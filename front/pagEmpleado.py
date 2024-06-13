import streamlit as st
from back.crud import obtener_empleado_correo, crear_empleado, verificar_empleado_registrado, correo_valido, \
    encriptar_contrasenia
from database.create_database import session

def pagEmpleado():
    # st.set_page_config(
    #     page_title= "Empleado"
    # )

    st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
    st.subheader('Empleado')

    choice = st.selectbox('Log In/Sing Up', ['Log In', 'Sign Up'])

    if choice == 'Log In':
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
                    else:
                        st.error("Correo o contraseña incorrectos")


    else:
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
                    empleado_registrado = obtener_empleado_correo(session, email) # Obtiene el registro de la bd
                    if empleado_registrado: # Si hay algun registro con ese correo en la bd:
                        st.error("El correo ya está registrado a otro empleado")
                    else: # Si no hay registro con ese correo, crea un nuevo empleado
                        sal, contrasenia_encriptada = encriptar_contrasenia(contrasenia)
                        crear_empleado(session, nombre, apellido, email, contrasenia_encriptada)
                        st.success("Registro exitoso")


    # if st.button("Volver a inicio"):

