from database.models import Empleado
import re
import bcrypt

def correo_valido(correo): # Verifica que el formato del correo sea valido
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, correo)

def obtener_empleado_by_correo(session, e_email): # Obtiene un registro de la bd que coincida con el correo dado
    return session.query(Empleado).filter(Empleado.correo == e_email).first()

def crear_empleado(session, e_nombre, e_apellido, e_email, e_contrasenia): # Crea un nuevo empleado
    nuevo_empleado = Empleado(nombre = e_nombre, apellido = e_apellido, correo = e_email, contrasena = e_contrasenia)
    session.add(nuevo_empleado)
    session.commit()

def verificar_empleado_registrado(session, correo, contrasenia): # Verifica los datos del empleado registrado
    empleado = obtener_empleado_by_correo(session, correo)
    if empleado and bcrypt.checkpw(contrasenia.encode('UTF-8'), empleado.contrasena):
        return empleado
    return None


def encriptar_contrasenia(contrasenia): # Encripta la contraseña para guardarla en la bd
    bytes = contrasenia.encode('UTF-8')
    sal = bcrypt.gensalt() # se genera una sal (agrega un valor random a la contraseña para evitar que dos contraseñas iguales tengan el mismo hash)
    contrasenia_encriptada = bcrypt.hashpw(bytes, sal) # Genera el hash, con la sal(valor random) agregada
    return sal, contrasenia_encriptada

def verificar_contrasenia(contrasenia, contrasenia_encriptada): # Verifica la contraseña encriptada
    resultado = bcrypt.checkpw(contrasenia.encode('UTF-8'), contrasenia_encriptada) # Compara la contraseña dada con la contraseña encriptada en la bd
    return resultado