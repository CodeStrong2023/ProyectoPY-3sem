import streamlit as st
from front.pagEmpleado import pagEmpleado
from front.SpagCliente import pagcliente


st.set_page_config(
    page_title= "Inicio"
)

st.title('BIENVENIDOS AL ESTACIONAMIENTO DE BUGBUSTERS')
st.subheader('Proyecto Python')
role = st.selectbox(
    'Seleccione su rol:',
    [None, 'Empleado', 'Cliente'],
    )

if role == 'Cliente':
    pagcliente()
elif role == 'Empleado':
    pagEmpleado()
else:
    pass