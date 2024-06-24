import streamlit as st
from sqlalchemy.orm import sessionmaker
from database.create_database import session
from database.models import Estacionamiento, Vehiculo, Cliente


def liberar_espacio(espacio_id):
    vehiculo = session.query(Vehiculo).filter_by(espacio_id=espacio_id).first()
    if vehiculo:
        session.delete(vehiculo)
        session.commit()

    espacio = session.query(Estacionamiento).filter_by(espacio=espacio_id).first()
    if espacio:
        espacio.disponibilidad = True
        session.commit()

def pag_empleado_est():
    estacionamientos = session.query(Estacionamiento).all()

    for espacio in estacionamientos:
        with st.expander(f"Espacio {espacio.espacio} - {'Disponible' if espacio.disponibilidad else 'Ocupado'}"):
            if espacio.disponibilidad:
                st.write("Este espacio está disponible.")
            else:
                vehiculo = session.query(Vehiculo).filter_by(espacio_id=espacio.espacio).first()
                cliente = session.query(Cliente).filter_by(id=vehiculo.cliente_id).first()
                st.write(f"**Patente:** {vehiculo.patente}")
                st.write(f"**Modelo:** {vehiculo.marca_modelo}")
                st.write(f"**Teléfono Cliente:** {cliente.telefono_cliente}")
                st.write(f"**Nombre Cliente:** {cliente.nombre}")
                st.write(f"**Hora Entrada:** {vehiculo.hora_entrada}")
                st.write(f"**Hora Salida:** {vehiculo.hora_salida}")

                liberar_button = st.button(f'Liberar Espacio {espacio.espacio}', key=f'liberar_{espacio.espacio}')
                if liberar_button:
                    liberar_espacio(espacio.espacio)