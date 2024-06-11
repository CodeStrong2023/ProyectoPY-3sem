import streamlit as st

showSidebarNavigation = False

st.set_page_config(
    page_title= "Inicio"
)
st.sidebar.page_link('homepage.py', label='Inicio')
st.sidebar.page_link('pages/pagEmpleado.py', label='Empleado')
st.sidebar.page_link('pages/SpagCliente.py', label='Cliente')


st.title('BIENVENIDOS AL ESTACIONAMIENTO DE BUGBUSTERS')
st.subheader('Proyecto Python')
role = st.selectbox(
    'Seleccione su rol:',
    [None, 'Empleado', 'Cliente'],
    )

if role == None:
    pass
elif role == 'Empleado':
    st.switch_page('pages/pagEmpleado.py')
else:
    st.switch_page('pages/SpagCliente.py')