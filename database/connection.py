import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
def get_engine():
    return create_engine(DATABASE_URL)

def get_connection():
    return psycopg2.connect(DATABASE_URL)
