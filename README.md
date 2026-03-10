# UnstableREM 👁️
Copyright (c) 2026 Harplume/BlueHarper
### LLM Tool-Calling Pipeline for Procedural World Generation in Roblox

A real-time pipeline that translates eye tracking data into dynamic Roblox world generation commands using LLM tool-calling — watched by 3,000+ people on YouTube.

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

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/UnstableREM.git
```

1. Open the project in Roblox Studio
2. Add your OpenRouter API key to the environment
3. Run the eye tracking input script
4. Hit Play in Roblox Studio and watch the world generate everytime you blink

---

## 📄 License
MIT

- Attribution is required to Harplume
- Free to use
