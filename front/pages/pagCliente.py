import streamlit as st

st.set_page_config(
    page_title= "Cliente"
)
st.sidebar.page_link('homepage.py', label='Inicio')
st.sidebar.page_link('pages/pagCliente.py', label='Cliente')

st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
st.subheader('Cliente')
with st.form(key='clienteLogIn'):
    nombre = st.text_input('Nombre')
    patente = st.text_input('Ingrese el número de patente')
    marca = st.text_input('¿Qué modelo es su vehículo?')
    st.write('Introduzca las horas de estacionamiento')
    t1 = st.time_input(label='Desde las:', value=None)
    t2 = st.time_input(label='Hasta las:', value=None)
    st.write(f'Usted va a quedarse desde las: {t1}, hasta las: {t2}')
    espacio = st.number_input(label='Por favor, elija un lugar de estacionamiento (1-20):', min_value=1, max_value=20)
    st.form_submit_button('Registrar vehiculo')

if st.button("Volver a inicio"):
    st.switch_page('homepage.py')