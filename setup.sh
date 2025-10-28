#!/bin/bash

# ATS Resume Platform Setup Script

echo "================================"
echo "ATS Resume Platform Setup"
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo ""
echo "Step 1: Creating environment files..."

# Create backend .env file
if [ ! -f backend/.env ]; then
    cp backend/.env.example backend/.env
    echo "✓ Created backend/.env"
else
    echo "✓ backend/.env already exists"
fi

# Create frontend .env file
if [ ! -f frontend/.env ]; then
    cp frontend/.env.example frontend/.env
    echo "✓ Created frontend/.env"
else
    echo "✓ frontend/.env already exists"
fi

echo ""
echo "Step 2: Creating storage directories..."
mkdir -p storage/uploads storage/generated storage/recordings
echo "✓ Storage directories created"

echo ""
echo "Step 3: Building Docker images..."
docker-compose build
echo "✓ Docker images built"

echo ""
echo "Step 4: Starting services..."
docker-compose up -d
echo "✓ Services started"

echo ""
echo "Step 5: Waiting for services to be ready..."
sleep 10

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "Services are running at:"
echo "  Frontend: http://localhost:3000"
echo "  Backend API: http://localhost:8000"
echo "  API Docs: http://localhost:8000/docs"
echo "  Database: localhost:5432"
echo ""
echo "To stop services, run: docker-compose down"
echo "To view logs, run: docker-compose logs -f"
echo ""
