import cv2
import time
import threading
import math
from matplotlib.pyplot import gray
import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS
import mediapipe as mp
import winsound
import generateTerrain
import threading

import os
os.environ['GLOG_minloglevel'] = '2'

app = Flask(__name__)
CORS(app)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

state = {
    "face_detected": False,
    "eyes_closed": False,
    "last_seen": time.time()
}

@app.route("/state")
def get_state():
    return jsonify(state)

@app.route("/generate")
def get_generate():
    return generateTerrain.generate_scene()

def get_eye_mask(frame, landmarks, eye_indices, w, h):
    points = []
    for idx in eye_indices:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append([x, y])

    points = np.array(points, dtype=np.int32)

    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.fillConvexPoly(mask, points, 255)

    return mask

def eye_aspect_ratio(landmarks, eye_indices, w, h):
    def dist(i, j):
        x1, y1 = landmarks[i].x * w, landmarks[i].y * h
        x2, y2 = landmarks[j].x * w, landmarks[j].y * h
        return math.dist((x1, y1), (x2, y2))

    vertical1 = dist(eye_indices[1], eye_indices[5])
    vertical2 = dist(eye_indices[2], eye_indices[4])
    horizontal = dist(eye_indices[0], eye_indices[3])

    return (vertical1 + vertical2) / (2.0 * horizontal)

def pixelate_region(frame, mask, pixel_size=20):
    output = frame.copy()
    region = cv2.bitwise_and(frame, frame, mask=mask)
    
    h, w = region.shape[:2]
    temp = cv2.resize(region, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR)
    
    temp = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
    
    background = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    output = cv2.add(background, temp)
    
    return output

def get_eye_bbox_padded(landmarks, eye_indices, w, h, pad_x=0.35, pad_y=0.6):
    xs = [int(landmarks[idx].x * w) for idx in eye_indices]
    ys = [int(landmarks[idx].y * h) for idx in eye_indices]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    eye_w = x_max - x_min
    eye_h = y_max - y_min

    pad_px = int(eye_w * pad_x)
    pad_py = int(eye_h * pad_y + eye_h * 1.2)

    x1 = max(0, x_min - pad_px)
    x2 = min(w, x_max + pad_px)
    y1 = max(0, y_min - pad_py)
    y2 = min(h, y_max + pad_py)

    return x1, y1, x2, y2

def draw_sharingan(canvas, cx, cy, radius):
    cv2.circle(canvas, (cx, cy), radius, (0, 0, 200), -1)
    cv2.circle(canvas, (cx, cy), radius, (0, 0, 120), int(radius * 0.12))
    cv2.circle(canvas, (cx, cy), radius, (0, 0, 0), max(2, int(radius * 0.08)))
    pupil_r = int(radius * 0.28)
    cv2.circle(canvas, (cx, cy), pupil_r, (0, 0, 0), -1)
    for i in range(3):
        angle = math.radians(i * 120 - 90)
        orbit = radius * 0.52
        tx = int(cx + orbit * math.cos(angle))
        ty = int(cy + orbit * math.sin(angle))
        tomoe_r = int(radius * 0.18)
        cv2.circle(canvas, (tx, ty), tomoe_r, (0, 0, 0), -1)
        tail_angle = angle + math.radians(50)
        tail_orbit = radius * 0.38
        tail_x = int(cx + tail_orbit * math.cos(tail_angle))
        tail_y = int(cy + tail_orbit * math.sin(tail_angle))
        tail_r = int(radius * 0.10)
        cv2.circle(canvas, (tail_x, tail_y), tail_r, (0, 0, 0), -1)
    cv2.circle(canvas, (cx, cy), int(radius * 0.45), (0, 0, 80), max(1, int(radius * 0.04)))


def apply_horizontal_stretch(region, stretch_factor=1.6):
    h, w = region.shape[:2]
    cx, cy = w / 2.0, h / 2.0

    map_x = np.zeros((h, w), dtype=np.float32)
    map_y = np.zeros((h, w), dtype=np.float32)

    for y in range(h):
        for x in range(w):
            nx = (x - cx) / cx
            ny = (y - cy) / (cy if cy > 0 else 1)
            src_nx = nx / stretch_factor
            src_x = src_nx * cx + cx
            src_y = y

            map_x[y, x] = src_x
            map_y[y, x] = src_y

    stretched = cv2.remap(region, map_x, map_y, interpolation=cv2.INTER_LINEAR,
                          borderMode=cv2.BORDER_REPLICATE)
    return stretched


def apply_eye_censorship(frame, landmarks, left_eye_indices, right_eye_indices, w, h):
    output = frame.copy()

    lx1, ly1, lx2, ly2 = get_eye_bbox_padded(landmarks, left_eye_indices, w, h)
    rx1, ry1, rx2, ry2 = get_eye_bbox_padded(landmarks, right_eye_indices, w, h)

    for (ex1, ey1, ex2, ey2), eye_indices in [
        ((lx1, ly1, lx2, ly2), left_eye_indices),
        ((rx1, ry1, rx2, ry2), right_eye_indices),
    ]:
        ex1 = max(0, ex1); ey1 = max(0, ey1)
        ex2 = min(w, ex2); ey2 = min(h, ey2)
        if ex2 <= ex1 or ey2 <= ey1:
            continue

        eye_region = output[ey1:ey2, ex1:ex2].copy()
        eh, ew = eye_region.shape[:2]
        ecx, ecy = ew // 2, eh // 2
        radius = min(ew, eh) // 2

        sharingan_canvas = eye_region.copy()
        draw_sharingan(sharingan_canvas, ecx, ecy, radius)
        eye_region = cv2.addWeighted(eye_region, 0.15, sharingan_canvas, 0.85, 0)
        eye_region = apply_horizontal_stretch(eye_region, stretch_factor=1.8)

        output[ey1:ey2, ex1:ex2] = eye_region

    band_x1 = min(lx1, rx1)
    band_x2 = max(lx2, rx2)
    band_y1 = min(ly1, ry1)
    band_y2 = max(ly2, ry2)

    band_x1 = max(0, band_x1)
    band_x2 = min(w, band_x2)
    band_y1 = max(0, band_y1)
    band_y2 = min(h, band_y2)

    if band_x2 > band_x1 and band_y2 > band_y1:
        white_bar = np.ones_like(output[band_y1:band_y2, band_x1:band_x2], dtype=np.uint8) * 255
        output[band_y1:band_y2, band_x1:band_x2] = cv2.addWeighted(
            output[band_y1:band_y2, band_x1:band_x2], 0.35,
            white_bar, 0.65,
            0
        )
        cv2.rectangle(output, (band_x1, band_y1), (band_x2, band_y2), (255, 255, 255), 2)

    return output



EAR_THRESHOLD = 0.15
EYE_CLOSED_TIME = 0.01

reset_timer = None

def reset_eyes_local():
    global reset_timer
    state["eyes_closed"] = False
    reset_timer = None

def camera_loop():
    global reset_timer
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            state["face_detected"] = True
            state["last_seen"] = time.time()

            left_eye_mask = get_eye_mask(frame, landmarks, LEFT_EYE, w, h)
            right_eye_mask = get_eye_mask(frame, landmarks, RIGHT_EYE, w, h)
            eye_mask = cv2.bitwise_or(left_eye_mask, right_eye_mask)
            kernel = np.ones((7, 7), np.uint8)
            eye_mask = cv2.dilate(eye_mask, kernel, iterations=1)
            face_mask = cv2.bitwise_not(eye_mask)
            frame = pixelate_region(frame, face_mask, pixel_size=30)
            frame = apply_eye_censorship(frame, landmarks, LEFT_EYE, RIGHT_EYE, w, h)

            ear_left = eye_aspect_ratio(landmarks, LEFT_EYE, w, h)
            ear_right = eye_aspect_ratio(landmarks, RIGHT_EYE, w, h)
            ear = (ear_left + ear_right) / 2

            if ear < EAR_THRESHOLD:
                if reset_timer:
                    reset_timer.cancel()
                    reset_timer = None
                state["eyes_closed"] = True
                print("BLINKING rahhhhhh!!!!!")
            else:
                if state["eyes_closed"] and reset_timer is None:
                    reset_timer = threading.Timer(0.3, reset_eyes_local)
                    reset_timer.start()

            cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv2.putText(frame, f"Eyes Closed: {state['eyes_closed']}", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("Unstable REM", gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("=" * 50)
    print("STARTING UNSTABLE REM")
    print("=" * 50)
    print("Starting camera thread...")
    threading.Thread(target=camera_loop, daemon=True).start()
    time.sleep(1)
    print("Camera thread started!")
    print("=" * 50)
    app.run(host="127.0.0.1", port=5000, debug=False)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()