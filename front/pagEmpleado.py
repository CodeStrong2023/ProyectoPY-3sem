import streamlit as st
from back.logica import crear_empleado, verificar_empleado_registrado, correo_valido, \
    encriptar_contrasenia, obtener_empleado_by_correo
from database.create_database import session
from front.pag_empleado_est import pag_empleado_est

def pagEmpleado():
    st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
    st.subheader('Empleado')

    if 'logged_in' in st.experimental_get_query_params():
        pag_empleado_est()
        st.stop()

    login_status = False

    choice = st.selectbox('Log in/sign up', ['Log In', 'Sign Up'])
    if choice == 'Log In':
        login_status = login()

    elif choice == 'Sign Up':
        signup()

    if login_status:
        st.experimental_set_query_params(logged_in=True)
        st.experimental_rerun()

def login():
    login = False
    with st.form(key='empleadoLogIn'):
        correo = st.text_input('Correo')
        contrasenia = st.text_input('Contraseña', type='password')
        btn_login = st.form_submit_button("Log In")

        if btn_login:
            if not correo or not contrasenia:
                st.error("Todos los campos son obligatorios")
            elif not correo_valido(correo): # valida el correo introducido
                st.error("El correo no es válido")
            else:
                usuario = verificar_empleado_registrado(session, correo, contrasenia) # Verifica los datos del empleado registrado
                if usuario:
                    st.success("Inicio de sesión exitoso")
                    login = True
                else:
                    st.error("Correo o contraseña incorrectos")
    return login

def signup():
    with st.form(key='empleadoSignUp'):
        nombre = st.text_input('Nombre/s')
        apellido = st.text_input('Apellido/s')
        email = st.text_input('Introduce tu e-mail')
        contrasenia = st.text_input('Introduce una constraseña', type ='password')
        submit_btn = st.form_submit_button("Sign Up")

        if submit_btn:
            if not nombre or not apellido or not email or not contrasenia:
                st.error("Todos los campos son obligatorios")
            elif not correo_valido(email):
                st.error("El correo no es válido")
            else:
                empleado_registrado = obtener_empleado_by_correo(session, email) # Obtiene el registro de la bd
                if empleado_registrado: # Si hay algun registro con ese correo en la bd:
                    st.error("El correo ya está registrado a otro empleado")
                else: # Si no hay registro con ese correo, crea un nuevo empleado
                    sal, contrasenia_encriptada = encriptar_contrasenia(contrasenia)
                    crear_empleado(session, nombre, apellido, email, contrasenia_encriptada)
                    st.success("Registro exitoso")