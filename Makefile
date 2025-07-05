# Makefile for SoundHub Recommendation API Docker management

# Variables
IMAGE_NAME = soundhub-rec-api
PORT = 8888
NETWORK = docker_app_network
CONTAINER_NAME = $(IMAGE_NAME)-container

.PHONY: help build run up down stop rm clean logs restart

help:  ## Show detailed help message
	@echo "SoundHub Recommendation API Docker Management"
	@echo "Usage: make [command]"
	@echo ""
	@echo "Available commands:"
	@echo "  make build    - Build Docker image (tag: $(IMAGE_NAME))"
	@echo "  make run      - Build and run container in detached mode (port: $(PORT))"
	@echo "  make up       - Alias for 'run'"
	@echo "  make start    - Start existing container"
	@echo "  make stop     - Stop running container (without removal)"
	@echo "  make rm       - Remove stopped container"
	@echo "  make down     - Stop and remove container (stop + rm)"
	@echo "  make clean    - Remove image and all related containers"
	@echo "  make logs     - Show container logs (follow mode)"
	@echo "  make restart  - Rebuild and restart container"
	@echo "  make ps       - Show running containers for this project"

build:  ## Build the Docker image
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .
	@echo "Image built successfully: $(IMAGE_NAME)"

run: build start  ## Run container (with build dependency)
	@echo "Container started successfully. Access API at http://localhost:$(PORT)"

up: run  ## Alias for run

start:  ## Start existing container
	@echo "Starting Docker container..."
	docker start $(CONTAINER_NAME)

stop:  ## Stop container (without removal)
	@echo "Stopping container..."
	@docker stop $(CONTAINER_NAME) 2>/dev/null || true
	@echo "Container stopped (not removed)"

rm:  ## Remove stopped container
	@echo "Removing container..."
	@docker rm $(CONTAINER_NAME) 2>/dev/null || true
	@echo "Container removed"

down: stop rm  ## Stop and remove container

clean: down  ## Remove image and containers
	@echo "Removing Docker image..."
	@docker rmi $(IMAGE_NAME) 2>/dev/null || true
	@echo "Cleanup complete - all containers and image removed"

logs:  ## Show container logs
	@echo "Showing logs for container $(CONTAINER_NAME):"
	@docker logs -f $(CONTAINER_NAME)

restart: down run  ## Rebuild and restart container
	@echo "Container restarted"

ps:  ## Show project containers
	@echo "Running containers for $(IMAGE_NAME):"
	@docker ps --filter "name=$(CONTAINER_NAME)"