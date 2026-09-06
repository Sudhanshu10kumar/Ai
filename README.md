# Network Security

A Python package skeleton for a network security project. The repository currently includes package structure, dependency management, logging utilities, and a custom exception class that records the source file and line number for runtime errors.

## Project Structure

```text
.
├── networksecurity/
│   ├── cloud/
│   ├── components/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   │   └── exception.py
│   ├── logging/
│   │   └── logger.py
│   ├── pipeline/
│   └── utils/
├── requirements.txt
├── setup.py
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- A virtual environment is recommended

Project dependencies are listed in `requirements.txt`:

```text
python-dotenv
pandas
numpy
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the package in editable mode for local development:

```bash
pip install -e .
```

## Environment Variables

The root `.env` file contains local development defaults. Update values as needed for your machine or deployment environment.

```bash
ENVIRONMENT=development
PROJECT_NAME=networksecurity
PYTHONPATH=.
LOG_LEVEL=INFO
LOG_DIR=logs
```

Do not commit real credentials, database URLs, API keys, passwords, or cloud secrets in `.env`.

## Usage

Import package utilities from `networksecurity` in your Python code.

Example for the custom exception helper:

```python
import sys
from networksecurity.exception.exception import NetworkSecurityException

try:
    1 / 0
except Exception as exc:
    raise NetworkSecurityException(exc, sys)
```

Example for logging:

```python
from networksecurity.logging import logger

logger.logging.info("Application started")
```

The current logger writes timestamped log files under a `logs/` directory created from the current working directory.

## Build

Build package artifacts:

```bash
python setup.py build
```

## Development Notes

- Keep source code inside the `networksecurity/` package.
- Add new dependencies to `requirements.txt`.
- Keep generated files, virtual environments, caches, logs, and local secrets out of git.
- Use `.env` for local configuration only.

## Author

Sudhanshu Kumar
