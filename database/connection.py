import psycopg2
from sqlalchemy import create_engine

def get_engine():
    DATABASE_URL = "postgresql://postgres:admin@localhost/estacionamiento"
    return create_engine(DATABASE_URL)

def get_connection():
    DATABASE_URL = "postgresql://postgres:admin@localhost/estacionamiento"
    return psycopg2.connect(DATABASE_URL)
