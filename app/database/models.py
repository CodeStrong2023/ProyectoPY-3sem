from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    contrasena = Column(String(50))
    estacionamientos = relationship("Estacionamiento", back_populates="empleado")


class Estacionamiento(Base):
    __tablename__ = 'estacionamiento'

    espacio = Column(Integer, primary_key=True)
    disponibilidad = Column(Boolean)
    empleado_id = Column(Integer)
    empleado = relationship("Empleado", back_populates="estacionamientos")
    vehiculos = relationship("Vehiculo", back_populates="estacionamiento")


