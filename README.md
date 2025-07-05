## Stack
- **Djando**: Framework principal
- **RDF**: Framework principal para crear la api


# Mejoras
- Authenticacion usuarios admin y con JWT, OAuth u otra
- nuevas tablas para cada banco para aumentar eficiencia 
- validaciones de datos mas detalladas.
- La memoria de los mensajes creo que se podria guardar de mejor manera.
- Ejemplo bien basico podria mejorarse infinidad de cosas para potenciarlo, traer info de algna api por ejemplo deudas, es importante ver si la persona realmente esta interesada por lo que definir parametros seria indispensables, esta api podria conectar con un servicio de mensajeria como whatsaap para darle funcionalidad real, el modelo de chatgpt realmente es bien sencillo se podria potenciar con parametros bien estudiados.
- Validar mas y mejores filtros para el modelo de open ai, tal ves hacer una seleccion mas interesante.

# Suposiciones
- El la data de las deudas del cliente se carga de api que no tengo disponible por lo que estara "Pre cargada"

# Ejecutar
- clonar el proyecto, 
- tener instalado python 3.10 en adelante
- crear y activar un entorno virtual (opcional)
- se instalan las depencias pip install -r requirements.txt
- se corre el proyecto con python manage.py runserver

# Modelo de Open Ai
- se escogio el modelo gpt-4-turbo por ser suficiente para realizar el trabajo, ademas de ser rapido y un coste acorde.

# Apoyo de chatGPT
- Utilice ayuda para crear la cuenta de GCP y para el deploy de la app