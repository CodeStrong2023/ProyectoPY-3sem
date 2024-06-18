from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#conexión a la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost/estacionamiento"
engine = create_engine(DATABASE_URL)

#crea las tablas en la base de datos
Base.metadata.create_all(engine)

#sesion con SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

#cerrar sesion despues de usarla
session.close()
