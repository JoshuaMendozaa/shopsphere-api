# Makefile for managing the Shopsphere API project
.PHONY: install dev-install test lint format clean run docker-up docker-down

# Basic installation of dependencies
install:
	pip install -r requirements.txt

# Installation of development dependencies
dev-install:
	pip install -r requirements-dev.txt

# Run tests with pytest
test:
	PYTHONPATH=. pytest --cov=app --cov-report=html --cov-report=term-missing

# Lint the codebase
lint:
	flake8 app tests
	mypy app
	black --check app tests
	isort --check-only app tests

# Format the codebase
format:
	black app tests
	isort app tests

# Clean up Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage htmlcov/ .pytest_cache/

# Run the application
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start Docker containers
docker-up:
	docker-compose up -d

# Stop Docker containers
docker-down:
	docker-compose down

# Database migration commands
migrate:
	alembic upgrade head
	
create-migration:
	@if [ -z "$(name)" ]; then \
		echo "Usage: make create-migration name='your migration message'"; \
		exit 1; \
	fi
	alembic revision --autogenerate -m "$(name)"

migration-history:
	alembic history --verbose

migration-current:
	alembic current

downgrade:
	@if [ -z "$(to)" ]; then \
		echo "Usage: make downgrade to=revision_id"; \
		exit 1; \
	fi
	alembic downgrade $(to)

# Database utilities
db-reset:
	alembic downgrade base
	alembic upgrade head

db-seed:
	python scripts/seed_db.py