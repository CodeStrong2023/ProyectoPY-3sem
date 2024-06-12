import streamlit as st

from back.crud import obtener_empleado_correo, crear_empleado
from back.database.create_database import Session

st.set_page_config(
    page_title= "Empleado"
)

st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
st.subheader('Empleado')

choice = st.selectbox('Log In/Sing Up', ['Log In', 'Sign Up'])

if choice == 'Log In':
    with st.form(key='empleadoLogIn'):
        correo = st.text_input('Correo'),
        contrasenia = st.text_input('Contraseña', type='password'),
        st.form_submit_button("Log In")
else:
    with st.form(key='empleadoSignUp'):
        nombre = st.text_input('Nombre/s'),
        apellido = st.text_input('Apellido/s'),
        telefono = st.text_input('Telefono'),
        email = st.text_input('Introduce tu e-mail'),
        contrasenia = st.text_input('Introduce una constraseña', type ='password'),
        st.form_submit_button("Sign Up")

        if st.form.submit_button:
            with Session() as session:
                empleado_registrado = obtener_empleado_correo(session, email)
                if empleado_registrado:
                    st.error("El correo ya está registrado a otro empleado")
                else:
                    crear_empleado(session, nombre, apellido, telefono, email, contrasenia)
                    st.success("Registro exitoso")
    
if st.button("Volver a inicio"):
    st.switch_page('homepage.py')
