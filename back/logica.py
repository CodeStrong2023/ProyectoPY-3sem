from database.create_database import session
from database.models import Empleado, Estacionamiento, Vehiculo
import re
import bcrypt

# Lógica para formulario de log in y sign up
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


# Lógica para registrar vehiculo

def verificar_disponibilidad(selected_space): # Verifica si el atributo disponibilidad esta en true o false (ocupado o no)
    espacio_disponible = session.query(Estacionamiento).filter(
        Estacionamiento.espacio == selected_space,
        Estacionamiento.disponibilidad == True
    ).first()
    return espacio_disponible

def verificar_horario(selected_space, hora_entrada_dt, hora_salida_dt): # verifica si el espacio esta ocupado en las horas solicitadas
    overlap = session.query(Vehiculo).filter(
        Vehiculo.espacio_id == selected_space,
        Vehiculo.hora_salida > hora_entrada_dt,
        Vehiculo.hora_entrada < hora_salida_dt
    ).first()
    return overlap