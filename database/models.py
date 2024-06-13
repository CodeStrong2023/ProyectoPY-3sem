from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    correo = Column(String(100))
    contrasena = Column(String(255))


class Estacionamiento(Base):
    __tablename__ = 'estacionamiento'

    espacio = Column(Integer, primary_key=True)
    disponibilidad = Column(Boolean)
    vehiculos = relationship("Vehiculo", back_populates="estacionamiento", uselist=False);


class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    patente = Column(String(10), primary_key=True)
    marca_modelo = Column(String(100))
    telefono_cliente = Column(String(20))
    hora_entrada = Column(DateTime)
    hora_salida = Column(DateTime)
    espacio_id = Column(Integer, ForeignKey('estacionamiento.espacio'))
    estacionamiento = relationship("Estacionamiento", back_populates="vehiculos")

