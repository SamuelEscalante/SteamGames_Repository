"""
Database Connection Utility

This module provides a utility function to establish a connection to a PostgreSQL database using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import json
import os
import sys


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
    credentials : dict
        A dictionary containing the database connection credentials

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
        engine = create_engine(url)
        print(f'Conected successfully to database {db}!')
        return engine
    except SQLAlchemyError as e:
        print(f'Error: {e}')

"""
 Make sure to replace the placeholder credentials with your actual database credentials.
"""