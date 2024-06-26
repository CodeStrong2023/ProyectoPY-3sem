import streamlit as st
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from database.create_database import session
from database.models import Vehiculo, Estacionamiento, Cliente
from back.logica import verificar_disponibilidad, verificar_horario
from streamlit_autorefresh import st_autorefresh

# Inicializar st.session_state
if 'selected_space' not in st.session_state:
    st.session_state.selected_space = None

if 't2' not in st.session_state:
    st.session_state.t2 = None

def pagcliente():
    st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
    st.subheader('Cliente')

    col1, col2 = st.columns(spec=[2, 1], gap="large")

    if session.query(Estacionamiento).count() == 0:
        for i in range(1, 21):
            espacio = Estacionamiento(espacio=i, disponibilidad=True)
            session.add(espacio)
        session.commit()

    with col1:
        with st.form(key='clienteLogIn'):
            nombre = st.text_input('Nombre')
            telefono = st.text_input('Teléfono')
            patente = st.text_input('Ingrese el número de patente').upper()
            marca = st.text_input('¿Qué modelo es su vehículo?')
            st.write('Introduzca las horas de estacionamiento')
            t1 = st.time_input(label='Desde las:', value=None)
            t2 = st.time_input(label='Hasta las:', value=None)
            if t1 and t2:
                st.write(f'Usted va a quedarse desde las: {t1}, hasta las: {t2}')
            submit_button = st.form_submit_button('Registrar vehiculo')

            form_complete = nombre != "" and telefono != "" and patente != "" and marca != "" and t1 is not None and t2 is not None

            if submit_button and form_complete:
                hoy = datetime.now().date()
                ahora = datetime.now().time()

                hora_entrada_dt = datetime.combine(hoy, t1)
                hora_salida_dt = datetime.combine(hoy, t2)

                if t1 < ahora:
                    st.error('La hora de entrada no puede ser menor a la hora actual.')
                    return

                if t2 <= t1:
                    st.error('La hora de salida no puede ser menor o igual a la hora de entrada.')
                    return

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

                cliente = session.query(Cliente).filter_by(nombre=nombre).first()
                if not cliente:
                    cliente = Cliente(
                        nombre=nombre,
                        telefono_cliente=telefono)
                    session.add(cliente)
                    session.commit()
                    session.refresh(cliente)

                vehiculo = Vehiculo(
                    patente=patente,
                    marca_modelo=marca,
                    hora_entrada=hora_entrada_dt,
                    hora_salida=hora_salida_dt,
                    cliente_id=cliente.id,
                    espacio_id=selected_space
                )

                session.add(vehiculo)
                session.commit()
                st.success('Vehículo registrado exitosamente')

                espacio = session.query(Estacionamiento).filter_by(espacio=selected_space).first()
                espacio.disponibilidad = False
                session.commit()

                # Guardar t2 en st.session_state para el contador
                st.session_state.t2 = t2

            elif submit_button and not form_complete:
                st.error("Por favor complete todos los campos del formulario.")

    with col2:
        st.write('Seleccione el número de estacionamiento:')
        selected_station = st.radio('Estacionamientos', options=list(range(1, 21)))

        if st.button('Seleccionar'):
            st.session_state.selected_space = selected_station
            st.success(f'Se ha seleccionado el estacionamiento número: {selected_station}')

    if 't2' in st.session_state and st.session_state.t2 is not None:
        ahora = datetime.now()
        t2 = datetime.combine(ahora.date(), st.session_state.t2)

        if ahora < t2:
            tiempo_restante = t2 - ahora
            horas, resto = divmod(tiempo_restante.seconds, 3600)
            minutos, segundos = divmod(resto, 60)
            tiempo_formateado = f"{horas:02}:{minutos:02}:{segundos:02}"
            st.write(f'Tiempo restante: {tiempo_formateado}')

            st_autorefresh(interval=1000, key='contador_autorefresh')
        else:
            st.write('Tu tiempo en nuestro estacionamiento concluyó.')
