# Proyecto Integrador Tercer Semestre TUP UTNFRSR
## Estacionamiento BugBusters 🚗🅿️
Este proyecto está enfocado a un estacionamiento el cual posee una interfaz para el cliente donde podrá ingresar los datos tanto del cliente, como del vehículo, seleccionar el tiempo y el espacio del stacionamiento donde desea estacionar. También cuenta con una interfaz para el empleado el cual puede registrarse e iniciar sesión. Una vez que inicia sesión puede acceder a la visualización de todos los espacios del estacionamiento y ver cuales estan ocupados y cuales no, además de poder ver los datos de los vehículos estacionados.
### Pasos para la ejecución ⚙️
1. Clonar el repositorio.

   ```git clone https://github.com/CodeStrong2023/ProyectoPY-3sem.git```
2. Moverse a la carpeta del proyecto.
   
    ```cd ProyectoPy-3sem```
  
3. Renombra el archivo `.env.example` a `.env`. Luego abre el archivo y actualiza con tus propios datos

   ```cp .env.example .env```
   
4. Instala las dependencias del proyecto.
   
   ```pip install -r requirements.txt```

5. Ejecuta el proyecto

   ```python -m streamlit run homepage.py```
### Tecnologías utilizadas 💻
- Python
- Streamlit
- PostgreSQL
