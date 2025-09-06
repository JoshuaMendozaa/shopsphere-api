"""
Database management script using Alembic for ShopSphere API.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command):
    """Run a shell command and return result."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False
    
def create_migration(message=None):
    """Create a new Alembic migration."""
    if not message:
        message = input("Enter migration message: ")
    
    command = f'alembic revision --autogenerate -m "{message}"'
    print(f"creating migration with message: {message}")
    return run_command(command)

def upgrade_db(revision="head"):
    """Upgrade the database to the latest revision or specified revision."""
    command = f'alembic upgrade {revision}'
    print(f"Upgrading database to revision: {revision}")
    return run_command(command)

def downgrade_db(revision="base"):
    """Downgrade the database to the specified revision."""
    command = f'alembic downgrade {revision}'
    print(f"Downgrading database to revision: {revision}")
    return run_command(command)

def show_history():
    """Show the migration history."""
    print("Migration history:")
    return run_command(command="alembic history")

def show_current():
    """Show the current database revision."""
    print("Current database revision:")
    return run_command(command="alembic current")

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python manage_db.py [create|upgrade|downgrade|history|current] [options]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "create":
        message = sys.argv[2] if len(sys.argv) > 2 else None
        create_migration(message)
    elif action == "upgrade":
        revision = sys.argv[2] if len(sys.argv) > 2 else "head"
        upgrade_db(revision)
    elif action == "downgrade":
        revision = sys.argv[2] if len(sys.argv) > 2 else "base"
        downgrade_db(revision)
    elif action == "history":
        show_history()
    elif action == "current":
        show_current()
    else:
        print(f"Unknown action: {action}")
        print("Usage: python manage_db.py [create|upgrade|downgrade|history|current] [options]")
        sys.exit(1)

if __name__ == "__main__":
    main()