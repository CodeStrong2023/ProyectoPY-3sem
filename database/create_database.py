from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from database.models import Base, Estacionamiento

#conexión a la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost/estacionamiento"
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
