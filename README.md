

# proyectoIV

# Bot de telegram que informa sobre actividades de la UGR #
[![Build Status](https://travis-ci.org/Antkk10/BotTelegramInfoActividadesUGR.svg?branch=master)](https://travis-ci.org/Antkk10/BotTelegramInfoActividadesUGR)
#### Descripción ####
Uso de un bot de Telegram para obtener información de las actividades que se realizan a lo largo de la semana.

1. El bot estará online todo el tiempo.
2. Recopilará la información de forma autónoma.
3. Responderá conforme se le pregunta.
4. Tendrá un entorno en pruebas para comprobar si el bot funciona correctamente.

#### Herramientas ####
Necesitamos una serie de herramientas para el correcto funcionamiento del bot.

1. Uso de un servicio en la nube para almacenar el bot y que funcione. **Azure o Amazon**
2. Posiblemente use como entorno de pruebas Docker.
3. Para la obtención de información aun no se ha decidido.
4. Uso de la API de Telegram.
5. Posiblemente use Python y algún otro lenguaje de programación que sirva para implementar el bot.
6. Uso de almacenes de datos para:
  * Almacen de datos que tenga la información de las próximas actividades de la universidad con su fecha, hora de inicio y descripción.
  * Almacen de datos con el histórico de las actividades de la universidad.
  * Almacen de datos con información de la cantidad de veces que se solicita obtener información sobre cada actividad.

Se puede valorar usar algún almacen de datos más.
El tipo de base de datos que se usará para cada cosa todavía no lo he decidido.

#### Integración continua ####

Para la integración continua he usado Travis-CI, lo he enlazado con mi cuenta de github. Para que Travis compruebe si nuestro código funciona correctamente he creado un archivo [.travis.yml](https://github.com/Antkk10/BotTelegramInfoActividadesUGR) indicandole el lenguaje de programación usado y el make de instalación y test del bot.

#### Make ####

He creado un archivo makefile para la instalación, test y ejecucición del bot. El make contiene:

    install:
    	pip install -r requirements.txt

    test:
    	cd ActividadesUGRBot && python test.py

    ejecutar:
    	cd ActividadesUGRBot && python actividadesUGR_bot.py
