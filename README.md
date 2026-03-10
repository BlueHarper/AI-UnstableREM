# UnstableREM 👁️
Copyright (c) 2026 Harplume/BlueHarper
### LLM Tool-Calling Pipeline for Procedural World Generation in Roblox

A real-time pipeline that translates eye tracking data into dynamic Roblox world generation commands using LLM tool-calling watched by 3,000+ people on YouTube.

---

## 🎬 Demo
> [Watch on YouTube](https://www.youtube.com/watch?v=u_h5yA71mVE&t)

---

## 🧠 How It Works

1. **Eye tracking** captures gaze input in real-time via Molmo2 8B
2. **OpenRouter API** routes the input through the LLM with pre-batched tool calls
3. **Tool calls** are parsed and sent to Roblox via HTTPService
4. **Roblox Studio** executes the generation commands in-engine using LuaU scripts

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Game Engine | Roblox Studio + LuaU |
| Vision Model | Meta: Llama 3.2 3B Instruct (via OpenRouter) |
| LLM Pipeline | OpenRouter API + Tool Calling + Pre-batching |
| Graphics | GIMP |
| Recording & Editing | OBS + CapCut |

---

## ⚡ Key Features

- **Pre-batching** — optimizes LLM API calls to reduce latency and improve generation responsiveness
- **Tool-calling pipeline** — structured LLM outputs drive in-game world generation commands
- **Real-time eye tracking** — gaze data feeds directly into the generation loop

---

## 🔧 Setup

1. **Clone the repo.** Make sure to open the cloned folder in your IDE.

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Add your API key** — create a `.env` file in the root:
```
   OPENROUTER_API_KEY=your_key_here
```

4. **Run the Flask server**
```bash
   python faceServer.py
```

> ⚠️ Windows only — `winsound` is used for audio feedback and is not supported on Mac/Linux.
> You may find an alternative OR completely remove winsound imports and winsound usages.

5. **You may now open the main.rbxl file and run it. You must save this as a game and then enable HTTPservice in game settings. You cannot enable this service unless you save this as a game.**

6. yayy congrats u got it working.
**Now, run the roblox game and it should be working!**

---

## 📄 License
MIT

- Attribution is required to Harplume
- Free to use
