# ATS Resume Platform

An AI-powered resume builder and mock interview platform that helps users create ATS-friendly resumes and practice mock interviews using local AI models.

## Features

- **ATS-Optimized Resumes**: Create resumes that pass ATS systems with AI-powered optimization
- **Mock Interviews**: Practice with AI-generated questions tailored to your target role
- **Instant Feedback**: Get detailed analysis and improvement suggestions
- **Local AI Models**: Uses Ollama for privacy-first AI processing
- **Multiple Templates**: Choose from professional resume templates

## Tech Stack

### Frontend
- React.js with React Router
- TailwindCSS for styling
- Axios for API communication
- Vite as build tool

### Backend
- FastAPI for REST API
- PostgreSQL for data storage
- SQLAlchemy for ORM
- Ollama for local LLM integration
- PyMuPDF for PDF parsing
- Whisper for speech-to-text

### Infrastructure
- Docker & Docker Compose for containerization
- PostgreSQL 15 for database

## Prerequisites

- Docker & Docker Compose
- Git
- 8GB RAM minimum (for Ollama)

## Quick Start

### 1. Clone the Repository
\`\`\`bash
git clone <repository-url>
cd ats-resume-platform
\`\`\`

### 2. Run Setup Script
\`\`\`bash
chmod +x setup.sh
./setup.sh
\`\`\`

This will:
- Create environment files
- Build Docker images
- Start all services
- Initialize the database

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Manual Setup (Without Script)

### 1. Create Environment Files
\`\`\`bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
\`\`\`

### 2. Start Services
\`\`\`bash
docker-compose up -d
\`\`\`

### 3. View Logs
\`\`\`bash
docker-compose logs -f
\`\`\`

## Project Structure

\`\`\`
ats-resume-platform/
├── frontend/                 # React application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── context/         # Context providers
│   │   └── utils/           # Utility functions
│   └── package.json
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── models/          # SQLAlchemy models
│   │   ├── routers/         # API routes
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utility functions
│   └── requirements.txt
├── database/                 # Database scripts
│   ├── schema.sql
│   └── seed_data.sql
├── storage/                  # File storage
│   ├── uploads/
│   ├── generated/
│   └── recordings/
├── docker-compose.yml
└── setup.sh
\`\`\`

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/signup` - User registration
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

### Resume
- `POST /api/resume/upload` - Upload resume
- `POST /api/resume/analyze-ats` - Analyze ATS compatibility
- `POST /api/resume/optimize` - Get optimization suggestions
- `POST /api/resume/generate-pdf` - Generate PDF resume
- `GET /api/resume/templates` - Get available templates

### Interview
- `POST /api/interview/setup` - Setup interview session
- `POST /api/interview/generate-questions` - Generate questions
- `POST /api/interview/analyze-response` - Analyze response
- `GET /api/interview/questions/{interview_id}` - Get questions
- `GET /api/interview/report/{interview_id}` - Get report

## Development

### Backend Development
\`\`\`bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
\`\`\`

### Frontend Development
\`\`\`bash
cd frontend
npm install
npm run dev
\`\`\`

## Database

### Initialize Database
\`\`\`bash
docker-compose exec backend python -m app.database
\`\`\`

### Access Database
\`\`\`bash
docker-compose exec postgres psql -U ats_user -d ats_resume_db
\`\`\`

## Troubleshooting

### Services won't start
- Check Docker is running: `docker ps`
- Check logs: `docker-compose logs`
- Ensure ports 3000, 8000, 5432 are available

### Database connection error
- Verify PostgreSQL is running: `docker-compose ps`
- Check DATABASE_URL in backend/.env
- Wait for database to be ready (check healthcheck)

### Frontend can't connect to backend
- Verify backend is running: `curl http://localhost:8000/health`
- Check VITE_API_URL in frontend/.env
- Check CORS settings in backend/app/main.py

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.
