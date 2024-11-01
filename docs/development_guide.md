# AIMetricMate Development Guide

## Setup Instructions

### Prerequisites
- Python 3.11+
- Docker (for containerized deployment)
- Azure Cosmos DB account
- Discord Developer account

### Local Development Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/aimetricmate.git
cd aimetricmate
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Development Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the code style guidelines
3. Run tests:
```bash
pytest
```

4. Format code:
```bash
black .
```

5. Create pull request

## Testing Procedures

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_specific.py

# Run with coverage
pytest --cov=aimetricmate
```

### Test Categories
1. Unit Tests: `/tests/unit/`
2. Integration Tests: `/tests/integration/`
3. End-to-End Tests: `/tests/e2e/`

## Deployment Process

### Local Docker Build
```bash
docker build -t aimetricmate .
docker run -d --env-file .env aimetricmate
```

### DigitalOcean Deployment
1. Push to main branch
2. CI/CD pipeline will:
   - Run tests
   - Build Docker image
   - Deploy to DigitalOcean
   - Run smoke tests

### Monitoring
- Check logs: `docker logs aimetricmate`
- Monitor metrics through DigitalOcean dashboard
- Set up alerts for critical metrics
