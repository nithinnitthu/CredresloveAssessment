# Cred-Resolve-assessment

# project-agent — Telugu Voice‑First Agent PoC (Updated)

This repo contains a PoC voice-first agent for Telugu, now with:
- Optional LLM integration (OpenAI-compatible) for reply polishing
- React + Vite frontend
- Docker + docker-compose to run backend + frontend
- Instructions in backend/.env.example for toggling LLM provider

## 🚀 Project Output

The links to my project that I hosted on...online 
(https://ibb.co/d4r0Y6ZG)



Quickstart (Docker)
1. Build and run:
   docker-compose up --build
2. Open frontend: http://localhost:5173 (or backend static UI at http://localhost:8000/ui if you prefer)
3. Use the React UI to record audio or provide mock text, confirm STT, and run the agent.

To enable OpenAI LLM:
1. Set backend/.env or environment variable LLM_PROVIDER=openai and OPENAI_API_KEY=your_key
2. Rebuild the backend image and restart docker-compose
