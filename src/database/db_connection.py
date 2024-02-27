"""
Database Connection Utility

This module provides a utility function to establish a connection to a PostgreSQL database using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database
import json
import os
import sys
import time

load_dotenv()
working_dir = os.getenv('WORK_DIR')

sys.path.append(working_dir)

with open(f'{working_dir}/credentials.json', 'r') as file:
    credentials = json.load(file)

def get_engine():
    """
    Establish a connection to a PostgreSQL database using SQLAlchemy

    Parameters
    ----------
    None

    Returns
    -------
    engine : sqlalchemy.engine.base.Engine
        A SQLAlchemy Engine object representing the established connection.

    Raises
    ------
    SQLAlchemyError: If there is an error establishing the database connection.

    """
    dialect = credentials.get('DIALECT')
    user = credentials.get('PGUSER')
    passwd = credentials.get('PGPASSWD')
    host = credentials.get('PGHOST')
    port = credentials.get('PGPORT')
    db = credentials.get('PGDB')

    url = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"
    try:

        if not database_exists(url):
            create_database(url)
            print(f"Database not found, let's create: {db}", end='', flush=True)
            for _ in range(5):  # Cambia el número según la duración deseada de la animación
                time.sleep(0.5)  # Ajusta el tiempo de espera según sea necesario
                print('.', end='', flush=True)
            engine = create_engine(url)
            print("created successfully.")
            return engine
        else:
            engine = create_engine(url)
            print(f'Conected successfully to {db}')
            return engine
    except SQLAlchemyError as e:
        print(f'Error: {e}')

"""
 Make sure to replace the placeholder credentials with your actual database credentials.
"""

