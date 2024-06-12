import streamlit as st

st.set_page_config(
    page_title= "Inicio"
)

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