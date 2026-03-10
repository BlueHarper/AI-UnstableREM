import requests
import os
import json
import threading
import queue
import random
import time

import generateRandom
import generateRandom2

from dotenv import load_dotenv
load_dotenv()

world_queue = queue.Queue(maxsize=15)
is_generating = False

with open('agent_prompt.txt', 'r') as file:
    file_content = file.read().strip()

def generate_ai_scene():
    """Generate scene using AI (runs in background)"""
    global is_generating
    
    try:
        is_generating = True
        print("AI REQUEST STARTED")
        
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_APIKEY')}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [
                    {
                        "role": "user",
                        "content": file_content
                    }
                ]
            }),
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(result)
            content = result['choices'][0]['message']['content']
            print(content)
            print("AI REQUEST COMPLETED")
            return content
        else:
            print(f"AI REQUEST FAILED: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"AI GENERATION ERROR: {e}")
        return None
    finally:
        is_generating = False

def background_generator():
    """Background thread that keeps the queue filled"""
    while True:
        try:
            if world_queue.qsize() < world_queue.maxsize:
                print(f"Queue size: {world_queue.qsize()}/{world_queue.maxsize} - Generating new AI world...")
                
                ai_world = generate_ai_scene()
                
                if ai_world:
                    world_queue.put(ai_world)
                    print(f"AI world added to queue! Queue size: {world_queue.qsize()}")
                else:
                    print("AI generation failed, waiting before retry...")
                    time.sleep(5)
            else:
                time.sleep(2)
                
        except Exception as e:
            print(f"Background generator error: {e}")
            time.sleep(5)

def generate_scene():
    """Main function called by Flask - returns immediately"""
    try:
        world = world_queue.get_nowait()
        print(f"✓ Serving AI world from queue! Remaining: {world_queue.qsize()}")
        return world
    except queue.Empty:
        print("⚠ Queue empty! Using random fallback")
        randomI = random.randint(0, 1)
        if randomI == 0:
            return generateRandom2.generate_terrain()
        else:
            return generateRandom.generate_random_scene()

generator_thread = threading.Thread(target=background_generator, daemon=True)
generator_thread.start()
print("Background world generator started!")