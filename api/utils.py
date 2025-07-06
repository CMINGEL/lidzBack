from itertools import cycle
import json
from decouple import config
from openai import OpenAI
from datetime import datetime, date
from dateutil import parser
from . import models
from django.core.exceptions import ValidationError

client = OpenAI(api_key=config("APIKEY"))

def chatBox(dicData, filtros=True):
	if filtros:
		filtros = f"""	
		3. Si tiene mensajes del dia anterior a hoy: {date.today()} no respondas para no ser invasivos.
		"""
	else:
		filtros=""

	jsonData= json.dumps(dicData)
	consulta = f"""
		Eres un asistente comercial cuya tarea es hacer seguimiento a clientes potenciales de forma profesional y respetuosa.
		Puedes insistir respondiendo los mismos mensajes si no hay respuesta del cliente.
		A continuación te entrego los datos disponibles del posible cliente en formato JSON: {jsonData}

		Este cliente ha visitado algunos de nuestros proyectos inmobiliarios en la web, entre ellos:
		- Arboleda 1
		- Arboleda 2
		- Cerro Lindo (este último tiene descuento en el pie)

		Quiero que generes un mensaje de seguimiento **corto, profesional y personalizado**, pero solo si se cumplen las siguientes condiciones:
		**Restricciones (analiza silenciosamente antes de responder):**
		1. Si la suma de las deudas del cliente es mayor a 15.000.000 CLP → responde solo dos llaves vacias.
		2. Si no tienes la respues di "Dejame averiguarlo" y termina la conversacion.
		{filtros}
		Ejecuta el análisis silenciosamente y si corresponde, genera el mensaje.
		"""

	response = client.chat.completions.create(
		model="gpt-4-turbo",
		messages=[
			{"role": "system", "content": "Eres un asistente comercial experto en análisis de clientes y ventas inmobiliarias."},
			{"role": "user", "content": consulta}]
    )
	return response.choices[0].message.content

def mensajeHoy(mensajes):
    if not mensajes:
        return False 

    mensajes_ordenados = sorted(mensajes, key=lambda x: parser.parse(x['sent_at']))
    ultimo_sent_at = parser.parse(mensajes_ordenados[-1]['sent_at'])
    ahora = datetime.now(tz=ultimo_sent_at.tzinfo)
    return ultimo_sent_at.date() >= ahora.date()

def validarRut(rut):
	try:
		rut = rut.upper()
		rut = rut.replace("-","")
		rut = rut.replace(".","")
		aux = rut[:-1]
		dv = rut[-1:]
	
		revertido = map(int, reversed(str(aux)))
		factors = cycle(range(2,8))
		s = sum(d * f for d, f in zip(revertido,factors))
		res = (-s)%11
	
		if str(res) == dv:
			return True
		elif dv=="K" and res==10:
			return True
		else:
			return False
	except:
		return False
	
def guardarMensaje(mensaje:str, client_id:int, role:str):
	try:
		if role not in ['agent', 'client']:
			raise ValidationError()
		
		if len(mensaje)<4:
			return True	#mensaje vacio no lo guarda

		cliente = models.Client.objects.get(pk=client_id)
		nuevoMensaje = models.Message.objects.create(client=cliente, text=mensaje, role=role)
		nuevoMensaje.save()
		return True
	except models.Client.DoesNotExist:
		print("manejar cliente no existe")
		return False
	except ValidationError:
		print("manejar role no valido")
		return False
	except:
		print("manejar otro problema")
		return False

