from database.models import Empleado

def obtener_empleado_correo(session, e_email):
    return session.query(Empleado).filter(Empleado.correo == e_email).first()

def crear_empleado(session, e_nombre, e_apellido, e_email, e_contrasenia):
    nuevo_empleado = Empleado(nombre = e_nombre, apellido = e_apellido, correo = e_email, contrasena = e_contrasenia)
    session.add(nuevo_empleado)
    session.commit()
