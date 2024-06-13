import streamlit as st
import numpy as np
import pandas as pd

def pagcliente():
    st.title('ESTACIONAMIENTO :blue[BUGBUSTERS]👻')
    st.subheader('Cliente')

    col1, col2 = st.columns(spec=[2, 1], gap= "large",)

    #    # Definir espacios de estacionamiento disponibles (por ahora simulados)
    #    num_filas = 5
    #    num_columnas = 5
    #    espacios_estacionamiento = np.random.choice([0, 1], size=(num_filas, num_columnas))
    #
    # Función para colorear los espacios de estacionamiento
    def colorear_espacio(estado):
        if estado == 1:
            return 'background-color: red'
        else:            
            return 'background-color: green'

        # Función para mostrar la interfaz gráfica de los espacios de estacionamiento
    #    def mostrar_estacionamiento(espacios_estacionamiento):
    #        st.write('Interfaz gráfica de los espacios de estacionamiento:')
    #        for i in range(num_filas):
    #            for j in range(num_columnas):
    #                st.markdown(
    #                    f'<div style="width: 50px; height: 50px; border: 1px solid black; {colorear_espacio(espacios_estacionamiento[i][j])}">{i+1}-{j+1}</div>',
    #                    unsafe_allow_html=True
    #                )


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
            st.form_submit_button('Registrar vehiculo')

        # Mostrar los espacios de estacionamiento en la interfaz
        # mostrar_estacionamiento(espacios_estacionamiento)


    with col2:

        data_df = pd.DataFrame(
            {
                "Estacionamiento": [
                    [ 1 , 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                ],
            }
        )

        st.data_editor(
            data_df,
            column_config={
            "Estacionamiento": st.column_config.ListColumn(
                label= 'Estacionamiento',
                width='large',
                ),
            },
            hide_index= True,
        )

