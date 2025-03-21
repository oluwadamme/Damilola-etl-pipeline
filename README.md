# Damilola ETL Pipeline

## Overview
This ETL (Extract, Transform, Load) pipeline is designed to efficiently process and manage data. It extracts data from various sources, applies transformations, and loads the processed data into a database.

## Features
- Data extraction from multiple sources
- Efficient transformation using `polars`
- Database integration with `SQLAlchemy` and `psycopg2`
- Configuration management using `.env` files
- Unit testing with `pytest`

## Project Structure
```
/etl_pipeline
│── .env                # Environment variables
│── .gitignore          # Git ignore file
│── pyproject.toml      # Project dependencies and metadata
│── poetry.lock         # Dependency lock file
│── README.md           # Project documentation
│── src/
│   ├── __init__.py     # Package initialization
│   ├── extract.py      # Extraction logic
│   ├── transform.py    # Data transformation logic
│   ├── load.py         # Load processed data into a database
│── tests/
│   ├── test_extract.py # Unit tests for extraction
│   ├── test_transform.py # Unit tests for transformation
│   ├── test_load.py    # Unit tests for loading
```

## Installation
### Prerequisites
- Python 3.13+
- Poetry package manager

### Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd etl_pipeline
   ```
2. Install dependencies:
   ```sh
   poetry install
   ```
3. Create a `.env` file based on `.env.example` and configure database settings.

## Usage
Run the ETL pipeline with:
```sh
python -m run_pipeline.py
```

To run tests:
```sh
pytest
```

## Dependencies
- `polars` (>=1.25.2,<2.0.0)
- `python-dotenv` (>=1.0.1,<2.0.0)
- `sqlalchemy` (>=2.0.39,<3.0.0)
- `psycopg2` (>=2.9.10,<3.0.0)
- `pytest` (>=8.3.5,<9.0.0)

## Author
**Damilola Adeniyi**


