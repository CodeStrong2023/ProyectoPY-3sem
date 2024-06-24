from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    correo = Column(String(100))
    contrasena = Column(LargeBinary)

class Estacionamiento(Base):
    __tablename__ = 'estacionamiento'

    espacio = Column(Integer, primary_key=True)
    disponibilidad = Column(Boolean)
    vehiculos = relationship("Vehiculo", back_populates="estacionamiento", uselist=False)

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    telefono_cliente = Column(String(20))
    vehiculos = relationship("Vehiculo", back_populates="cliente")

class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    patente = Column(String(10), primary_key=True)
    marca_modelo = Column(String(100))
    hora_entrada = Column(DateTime)
    hora_salida = Column(DateTime)
    espacio_id = Column(Integer, ForeignKey('estacionamiento.espacio'))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    estacionamiento = relationship("Estacionamiento", back_populates="vehiculos")
    cliente = relationship("Cliente", back_populates="vehiculos")


