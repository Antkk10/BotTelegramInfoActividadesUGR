

# proyectoIV

La descripción del proyecto se encuentra en la rama master del repositorio.

### Explicación del uso de las herramientas escogidas para el desarrollo del proyecto ###

1. El bot está en la nube para que los usuarios tengan siempre acceso a la información que ofrece el bot.
2. Docker: automatiza el despliegue de aplicaciones dentro de contenedores de software. Lo voy a utilizar porque ha sido comentado en clase y no conozco otro.
3. Uso de Telegram para que los usuarios puedan obtener información de actividades d ela universidad. La aplicación de Telegram es accesible a todo el mundo y muy usada para chatear entre otras tareas.
4. Para el desarrollo del bot voy a usar el lenguaje de programación Python. Es una de las opciones que se pueden usar y quiero aprender a programar en este lenguaje.
5. En el proyecto uso almacenes de datos para separar la información. Juan ha explicado en clase que es muy importante tener varias base de datos y que cada una maneja la información que le corresponde (explicada en README.md). Sobre que base de datos usar para cada una de las tres opciones, se está valorando.


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
