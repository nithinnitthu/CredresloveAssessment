# Frontend Dockerfile for Vite + React
FROM node:20-alpine

WORKDIR /app

# IMPORTANT: ensure devDependencies are installed
ENV NODE_ENV=development

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

