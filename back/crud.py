from back.database.models import Empleado

def obtener_empleado_correo(session, e_email):
    return session.query(Empleado).filter(Empleado.email == e_email).first()

def crear_empleado(session, e_nombre, e_apellido, e_telefono, e_email, e_contrasenia):
    nuevo_empleado = Empleado(nombre = e_nombre, apellido = e_apellido, telefono = e_telefono, email = e_email, contrasenia = e_contrasenia)
    session.add(nuevo_empleado)
    session.commit()
