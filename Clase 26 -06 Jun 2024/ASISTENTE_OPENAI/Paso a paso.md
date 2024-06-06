# Pasos para crear un asistente

1. Crear el ambiente (improtante asegurarse que Python este como variable de entorno)
```cmd
python -m venv david_env
```
2. Activar el ambiente

```cmd
.\david_env\Scripts\Activate.ps1
```
3. Crear el archivo requirements.txt con las dependencias
```cmd
requests==2.31.0
openai == 1.2.3
python-dotenv==1.0.0
```
4. Instalar las dependencias
```cmd 
pip install -r requirements.tx
```
5. Crear un archivo en formato `.env` para almacenar variables de entorno (pwd, Api keys, etc) colocando su api key
```cmd
OPENAI_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
6. Crear la configuracion del asistente en el archivo `Funciones.py`
7. Crear el asistente con el archivo `Asistente.py`
8. Correr el archivo `Conversacion.py`


