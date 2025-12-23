🎙️ Cred-Resolve-Assessment
Telugu Voice-First Agent (PoC)

A voice-first conversational agent Proof of Concept designed specifically for Telugu language interaction.
This project demonstrates a full-stack AI system with speech input, optional LLM-powered responses, and a modern web UI — packaged using Docker for easy deployment.

🚀 Project Highlights

🎤 Telugu Voice-First Interaction

🧠 Optional LLM Integration (OpenAI-compatible)

⚛️ React + Vite Frontend

🐳 Docker & Docker Compose Setup

🔁 Configurable backend using environment variables

📦 End-to-end PoC suitable for real-world AI agent systems

🧠 What This Project Does

User records Telugu speech via the browser

Backend processes audio → Speech-to-Text (STT)

Text is optionally sent to an LLM for response refinement

Final response is returned to the frontend UI

This architecture mirrors real voice-assistant / AI agent pipelines used in production systems.

🖼️ Project Output

🔗 Hosted Output / Demo Screenshot:
https://ibb.co/d4r0Y6ZG

(Shows the working UI and agent flow)

🏗️ Architecture Overview
🌐 Frontend (React + Vite)

Records audio input

Sends audio or mock text to backend

Displays processed agent responses

Lightweight, fast development setup using Vite

⚙️ Backend (Agent + STT + LLM Logic)

Handles audio/text input

Converts speech to text

Optional LLM-based reply polishing

Controlled via .env configuration

🐳 Deployment

Dockerized backend and frontend

One-command startup using docker-compose

📁 Project Structure
CredresloveAssessment/
├── backend/
│   ├── .env.example        # Environment config (LLM toggle)
│   ├── app/                # Agent + STT logic
│   └── Dockerfile
├── frontend/
│   ├── src/                # React UI
│   ├── index.html
│   └── Dockerfile
├── docker-compose.yml      # Dev setup
├── docker-compose.prod.yml # Production setup
├── DOCKER.md               # Docker instructions
└── README.md

⚡ Quickstart (Docker)
🔧 Build & Run
docker-compose up --build

🌍 Open the App

Frontend UI: http://localhost:5173

Backend UI (optional): http://localhost:8000/ui

🎤 How to Use

Open the frontend in your browser

Record Telugu audio or provide mock text

Confirm STT output

Run the agent and view the response

🤖 Enabling OpenAI LLM Integration (Optional)

By default, the agent can run without an LLM.
To enable OpenAI-compatible models:

1️⃣ Set environment variables

Edit backend/.env:

LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here

2️⃣ Rebuild & Restart
docker-compose up --build

💡 Why This Project Stands Out

✅ Voice-first design focused on Telugu, not English-only
✅ Clean separation of frontend, backend, and agent logic
✅ Configurable LLM usage (on/off switch)
✅ Dockerized for easy evaluation and deployment
✅ Strong foundation for government services, chatbots, or AI assistants

🧑‍💻 Tech Stack
Layer	Technology
Frontend	React, Vite
Backend	Python (Agent + STT logic)
AI / LLM	OpenAI-compatible (optional)
Deployment	Docker, Docker Compose
Input Mode	Voice + Text
📌 Use Cases

Telugu voice assistants

AI-powered service agents

Government / public service interfaces

Multilingual AI experimentation

Voice-enabled web applications

👨‍💻 Author

Anumandla Nithin Chandra
B.Tech CSE
Built as part of Cred-Resolve Assessment

🔗 GitHub: https://github.com/nithinnitthu
