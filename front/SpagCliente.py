import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from back.logica import verificar_disponibilidad, verificar_horario
from database.create_database import session
from database.models import Vehiculo

# Inicializar st.session_state
if 'selected_space' not in st.session_state:
    st.session_state.selected_space = None

def get_session():
    DATABASE_URL = "postgresql://postgres:1234@localhost/estacionamiento"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def pagcliente():
    st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
    st.subheader('Cliente')

    col1, col2 = st.columns(spec=[2, 1], gap="large")

    with col1:
        # Formulario de registro de vehículo
        with st.form(key='clienteLogIn'):
            nombre = st.text_input('Nombre')
            Telefono = st.text_input('Teléfono')
            patente = st.text_input('Ingrese el número de patente')
            marca = st.text_input('¿Qué modelo es su vehículo?')
            st.write('Introduzca las horas de estacionamiento')
            t1 = st.time_input(label='Desde las:', value=None)
            t2 = st.time_input(label='Hasta las:', value=None)
            st.write(f'Usted va a quedarse desde las: {t1}, hasta las: {t2}')
            submit_button = st.form_submit_button('Registrar vehiculo')

        if submit_button:
            hoy = datetime.now().date()
            hora_entrada_dt = datetime.combine(hoy, t1)
            hora_salida_dt = datetime.combine(hoy, t2)
            selected_space = st.session_state.get('selected_space')
            if not selected_space:
                st.error('Por favor, seleccione un espacio de estacionamiento.')
                return

            overlap = verificar_horario(selected_space, hora_entrada_dt, hora_salida_dt)
            if overlap:
                st.error('El espacio seleccionado está ocupado en el horario solicitado.')
                return

            disponibilidad = verificar_disponibilidad(selected_space)
            if not disponibilidad:
                st.error('El espacio seleccionado no está disponible.')
                return

            vehiculo = Vehiculo(
                patente=patente,
                marca_modelo=marca,
                telefono_cliente=Telefono,
                hora_entrada=hora_entrada_dt,
                hora_salida=hora_salida_dt,
                nombre=nombre,
                espacio_id=selected_space
            )

            session.add(vehiculo)
            session.commit()
            st.success('Vehículo registrado exitosamente')

            disponibilidad.disponibilidad = False # se actualiza la disponibilidad en la bd
            session.commit()

    with col2:
        # Mostrar los espacios de estacionamiento y permitir al usuario seleccionar uno
        st.write('Seleccione el número de estacionamiento:')
        selected_station = st.radio('Estacionamientos', options=list(range(1, 21)))

        # Actualizar st.session_state.selected_space cuando se seleccione un espacio
        if st.button('Seleccionar'):
            st.session_state.selected_space = selected_station
            st.success(f'Se ha seleccionado el estacionamiento número: {selected_station}')

