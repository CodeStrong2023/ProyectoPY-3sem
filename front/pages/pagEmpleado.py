import streamlit as st

st.set_page_config(
    page_title= "Empleado"
)
st.sidebar.page_link('homepage.py', label='Inicio')
st.sidebar.page_link('pages/pagEmpleado.py', label='Empleado')


st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
st.subheader('Empleado')

choice = st.selectbox('LogIn/SingUp', ['LogIn', 'SignUp'])

if choice == 'LogIn':
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
    
if st.button("Volver a inicio"):
    st.switch_page('homepage.py')
