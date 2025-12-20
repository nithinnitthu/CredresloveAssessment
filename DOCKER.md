# Docker Setup Guide

This project includes Docker configurations for both development and production environments.

## Folder Structure

```
.
├── backend/
│   ├── Dockerfile          # Development Dockerfile
│   ├── Dockerfile.prod     # Production Dockerfile
│   ├── requirements.txt    # Python dependencies
│   └── .dockerignore       # Files to exclude from Docker build
├── frontend/
│   ├── Dockerfile          # Development Dockerfile
│   ├── Dockerfile.prod     # Production Dockerfile
│   ├── package.json        # Node.js dependencies
│   └── .dockerignore       # Files to exclude from Docker build
├── docker-compose.yml      # Development compose file
└── docker-compose.prod.yml # Production compose file
```

## Development Setup

### Prerequisites
- Docker and Docker Compose installed

### Running in Development Mode

1. **Start both services:**
   ```bash
   docker-compose up
   ```

2. **Start in detached mode:**
   ```bash
   docker-compose up -d
   ```

3. **Rebuild images:**
   ```bash
   docker-compose build
   ```

4. **View logs:**
   ```bash
   docker-compose logs -f
   ```

5. **Stop services:**
   ```bash
   docker-compose down
   ```

### Development URLs
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

## Production Setup

### Building and Running Production Images

1. **Build production images:**
   ```bash
   docker-compose -f docker-compose.prod.yml build
   ```

2. **Start production services:**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. **View production logs:**
   ```bash
   docker-compose -f docker-compose.prod.yml logs -f
   ```

4. **Stop production services:**
   ```bash
   docker-compose -f docker-compose.prod.yml down
   ```

### Production URLs
- Frontend: http://localhost (port 80)
- Backend API: http://localhost:8000

### Environment Variables

Create a `.env` file in the root directory for production:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
TTS_PROVIDER=gtts
```

## Individual Service Commands

### Backend Only

**Development:**
```bash
cd backend
docker build -t backend-dev .
docker run -p 8000:8000 -v $(pwd):/app backend-dev
```

**Production:**
```bash
cd backend
docker build -f Dockerfile.prod -t backend-prod .
docker run -p 8000:8000 backend-prod
```

### Frontend Only

**Development:**
```bash
cd frontend
docker build -t frontend-dev .
docker run -p 5173:5173 -v $(pwd):/app frontend-dev
```

**Production:**
```bash
cd frontend
docker build -f Dockerfile.prod -t frontend-prod .
docker run -p 80:80 frontend-prod
```

## Dockerfile Details

### Backend Dockerfile
- Base image: `python:3.11-slim`
- Installs system dependencies (gcc, g++) for Python packages
- Installs Python dependencies from `requirements.txt`
- Exposes port 8000
- Development: Runs with hot-reload
- Production: Runs with multiple workers and non-root user

### Frontend Dockerfile
- Base image: `node:20-alpine`
- Installs Node.js dependencies
- Development: Runs Vite dev server
- Production: Multi-stage build with nginx to serve static files

## Troubleshooting

### Port Already in Use
If ports 8000, 5173, or 80 are already in use, modify the port mappings in `docker-compose.yml`:
```yaml
ports:
  - "8001:8000"  # Change host port
```

### Rebuild After Code Changes
In development, code changes are automatically reflected due to volume mounts. For production, rebuild the images:
```bash
docker-compose -f docker-compose.prod.yml build --no-cache
```

### View Container Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Clean Up
```bash
# Stop and remove containers
docker-compose down

# Remove volumes
docker-compose down -v

# Remove images
docker-compose down --rmi all
```

