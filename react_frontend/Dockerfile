# Multi-stage build for Vite React frontend
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* .npmrc* ./ 2>/dev/null || true
RUN npm ci || npm install
COPY . .
# Vite will read .env.production if present; otherwise relies on environment at build time
RUN npm run build

# Static server
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
# Default Nginx listens on 80; map to 3000 via docker-compose ports
EXPOSE 80
# Basic healthcheck
HEALTHCHECK CMD wget -qO- http://localhost/ || exit 1
