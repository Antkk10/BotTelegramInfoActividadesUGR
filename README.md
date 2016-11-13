

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
6. Uso de **Postgresql** como almacen de datos.

Se puede valorar usar algún almacen de datos más.

#### Integración continua ####

Para la integración continua he usado Travis-CI, lo he enlazado con mi cuenta de github. Para que Travis compruebe si nuestro código funciona correctamente he creado un archivo [.travis.yml](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/.travis.yml) indicandole el lenguaje de programación usado y el make de instalación y test del bot.

#### Make ####

He creado un archivo makefile para la instalación, test y ejecucición del bot. El make contiene:

    install:
    	pip install -r requirements.txt

    test:
    	cd ActividadesUGRBot && python test.py

    ejecutar:
    	cd ActividadesUGRBot && python actividadesUGR_bot.py

#### Despliegue ####

El despliegue lo he hecho en [Heroku](https://www.heroku.com). He configurado la aplicación creada en mi cuenta (la he llamado **actividadesugr**) para que cuando se realicen cambios en mi repositorio de github y pase los test de travis, estos cambios estén reflejados en la aplicación almacenada en Heroku.

Para que Heroku sepa como ejecutar el bot, necesita que creemos en el directorio raiz de nuestra aplicación el fichero [Procfile](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/Procfile) con el siguiente contenido:

    worker: cd ActividadesUGRBot && python actividadesUGR_bot.py

También he creado un archivo llamado **runtime.txt** para indicar la versión de python:

    python-2.7.12

La aplicación actualmente está operativa y se puede buscar en Telegram **@ActividadesUGRbot** y de momento tiene dos funcionalidades /start y /actividades (son simplemente de prueba para ver el funcionamiento del bot).
