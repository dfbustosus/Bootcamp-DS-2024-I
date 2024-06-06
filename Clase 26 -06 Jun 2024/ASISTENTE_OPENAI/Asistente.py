###################################################
# 1. Librerias
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
import os
from Funciones import gather_user_data, gather_reservation_data, not_talk
###################################################
# 2. Cargar variables entorno
load_dotenv();
openai_key= os.getenv("OPENAI_KEY");
#print(openai_key)
###################################################
# 3. Crear el cliente (permite la conexión con OPENAI)
client=OpenAI(api_key= openai_key);
###################################################
# 4. Crear el asistente
assistant = client.beta.assistants.create(
    name = "David Bot",
    instructions="No hagas supuestos acerca de los valores a utilizar en las funciones. Eres un aisstente que permite reservar en el restaurante Condorito.  Pregunta primero por nombre, apellido, email y telefono. Luego pregunta sobre los detalles de la reserva: fecha y hora. Finalmente si el usuario no quiere hablar mas termina la conversacion",
    model ="gpt-3.5-turbo-1106", # gpt-3.5-turbo-1106
    tools = [{"type":"function", "function":gather_user_data},
             {"type":"function", "function":gather_reservation_data},
             {"type":"function", "function": not_talk}]
)
print(assistant.id) # asst_UoTWfetExbajw40Yp6CVoFsZ
###################################################
# 5. Listar asistentes disponibles
mis_asistentes=client.beta.assistants.list(order="desc", limit="20")
print(mis_asistentes.data)
