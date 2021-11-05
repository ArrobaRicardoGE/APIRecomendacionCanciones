# APIRecomendacionCanciones
Proyecto para demostrar el uso e implementación de APIs

## Instrucciones de instalación
1. Clonar repositorio:
    - Con git: `git clone https://github.com/ArrobaRicardoGE/APIRecomendacionCanciones.git`
    - O bien, descargando el ZIP

2. Verificar que se tenga Python 3.9 instalado:
    - Usar `python --version` o `python3 --version`
    - Instalar o actualizar, según sea necesario

3. Crear un entorno virtual dentro de la carpeta del proyecto: 
    - En Windows: `python -m venv venv`
    - Más información en la [documentación de venv](https://docs.python.org/3/library/venv.html).

4. Activar el entorno e instalar dependencias:
    - Para activar en Windows: `.\venv\Scripts\activate`
    - Para instalar: `python -m pip install -r requirements.txt`

5. Obtener un OAuth token válido de la API de Spotify:
    - Registrarse en Spotify (**no se necesita cuenta premium**)
    - Acceder a https://developer.spotify.com/console/get-search-item/ y solictar el token
    - Sustituir en `spotify_api.py` la cadena `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` con el token obtenido (**NO COMPARTAS DICHO TOKEN**)

## Para correr la API de forma local
1. Ejecutar `python3 api.py`
2. Cuando esté ejecutandose, acceder a `http://127.0.0.1:5000/v1/recommend`, deberías de ver la respuesta a la solicitud 😊 (solo funciona desde tu computadora).
