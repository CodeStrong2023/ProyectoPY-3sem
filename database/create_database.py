from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Estacionamiento
import os
from dotenv import load_dotenv

load_dotenv()

#conexión a la base de datos
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

#crea las tablas en la base de datos
Base.metadata.create_all(engine)

#sesion con SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

if session.query(Estacionamiento).count() == 0:
    for i in range(1, 21):
        espacio = Estacionamiento(espacio=i, disponibilidad=True)
        session.add(espacio)
    session.commit()

session.close()
