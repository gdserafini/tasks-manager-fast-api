from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from config.settings import Settings
from src.model.exceptions import DatabaseConnectionError
import subprocess


engine = create_engine(Settings().DATABASE_URL)


def get_session(): # pragma: no cover
    with Session(engine) as session:
        yield session


def test_db_connection() -> None:
    try:
        with engine.connect() as connection:
            print(f'Successfully connection: {connection}')
            inspector = inspect(engine)
            if 'users' not in inspector.get_table_names():
                print('Not found db tables, running migrations...')
                subprocess.run(['alembic', 'upgrade', 'head'], check=True)
                print('Finished migrations.')
    except Exception as e:
        detail = f'Database connection error: {e}'
        raise DatabaseConnectionError(message=detail)
