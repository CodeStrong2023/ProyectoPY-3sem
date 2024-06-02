from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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
    __tablename__ = 'estacionamientos'

    espacio = Column(Integer, primary_key=True)
    disponibilidad = Column(Boolean)
    empleado_id = Column(Integer, ForeignKey('empleados.id'))
    empleado = relationship("Empleado", back_populates="estacionamientos")
    vehiculos = relationship("Vehiculo", back_populates="estacionamiento")


class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    patente = Column(String(10), primary_key=True)
    marca_modelo = Column(String(100))
    telefono_cliente = Column(String(20))
    tiempo = Column(Integer)
    espacio_id = Column(Integer, ForeignKey('estacionamientos.espacio'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    estacionamiento = relationship("Estacionamiento", back_populates="vehiculos")
    usuario = relationship("Usuario", back_populates="vehiculos")


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    correo = Column(String(100))
    vehiculos = relationship("Vehiculo", back_populates="usuario")

