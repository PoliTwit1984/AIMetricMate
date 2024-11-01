# AIMetricMate

AIMetricMate is a Discord bot designed to track and analyze AI development metrics, focusing on LLM cost analytics, GitHub Copilot usage monitoring, and prompt management.

## Features

- LLM cost tracking and analytics
- GitHub Copilot usage monitoring
- Prompt management system
- Project showcase capabilities
- Real-time analytics dashboard

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aimetricmate.git
cd aimetricmate
```

2. Set up virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the bot:
```bash
python -m aimetricmate
```

## Documentation

- [Project Overview](docs/project_overview.md)
- [Development Guide](docs/development_guide.md)
- [Database Schema](docs/database_schema.md)
- [API Documentation](docs/api_documentation.md)

## Development

### Prerequisites
- Python 3.11+
- Azure Cosmos DB account
- Discord Developer account
- Docker (for deployment)

### Testing
```bash
pytest
```

### Code Style
```bash
black .
```

## Deployment

### Docker
```bash
docker build -t aimetricmate .
docker run -d --env-file .env aimetricmate
```

### DigitalOcean
Automated deployment via GitHub Actions to DigitalOcean.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
