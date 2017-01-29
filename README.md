

# proyectoIV

# Bot de telegram que informa sobre actividades de la UGR #
[![Build Status](https://travis-ci.org/Antkk10/BotTelegramInfoActividadesUGR.svg?branch=master)](https://travis-ci.org/Antkk10/BotTelegramInfoActividadesUGR)
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

[![Azure](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/Documentacion/capturas/windows-azure.png)](botactividadesugr.azure.app)

[![Telegram bot](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/Documentacion/capturas/telegram2.png)](https://telegram.me/ActividadesUGRBot)
#### Descripción ####
Uso de un bot de Telegram para obtener información de las actividades que se realizan a lo largo de la semana.

1. El bot estará online todo el tiempo.
2. Responderá conforme se le pregunta.
3. Tendrá un entorno en pruebas para comprobar si el bot funciona correctamente.

#### Herramientas ####
Necesitamos una serie de herramientas para el correcto funcionamiento del bot.

1. Uso de un servicio en la nube para almacenar el bot y que funcione. **Azure**.
2. Posiblemente use como entorno de pruebas Docker.
3. Uso de la API de Telegram.
4. Uso de Python para desarrollar el bot.
5. Uso de **Postgresql** como almacen de datos.

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

El despliegue lo he hecho en [Heroku](https://www.heroku.com). Para hacer dicho despliegue instalamos la linea de comandos de heroku en nuestro terminal:

    wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

Posteriormente necesitamos loguearnos para poder desplegar la aplicación:

    heroku login

Creamos la aplicación:

    heroku apps:create --region eu actividadesugr

Para que Heroku sepa como ejecutar el bot, necesita que creemos en el directorio raiz de nuestra aplicación el fichero [Procfile](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/Procfile) con el siguiente contenido:

    worker: cd ActividadesUGRBot && python actividadesUGR_bot.py

También he creado un archivo llamado **runtime.txt** para indicar la versión de python:

    python-2.7.12

Para crear la base de datos (Postgresql) lo indicamos con el siguiente comando:

    heroku addons:create heroku-postgresql:hobby-dev --app actividadesugr

Para introducir los tokens que necesita nuestra aplicación que es el token de telegram y las credenciales para la base de datos usamos el comando:

    heroku config:set TOKEN=XXXX --app actividadesugr

Para desplegar la aplicación en heroku enlazamos nuestra aplicación al repositorio de github, y además le indicamos que si no pasa los test, no actualice nuestra aplicación en el despliegue. Esto se hace en la página de heroku, nuestra aplicación (actividadesugr), pestaña Deploy y lo asociamos al repositorio y pulsamos en la opción **Wait for CI to pass before deploy**

Para poner en funcionamiento la aplicación introducimos este comando:

    heroku ps:scale worker=1 --app actividadesugr

##### Aplicación #####

Para realizar consultas a la aplicación [Bot](https://telegram.me/ActividadesUGRBot) y tiene los comandos **/start** y **/actividades**

## Contenedores con Docker ##

Repositorio [Docker hub Actividades UGR bot](https://hub.docker.com/r/antkk/bottelegraminfoactividadesugr/)

Hay dos formas de instalar, la primera es colocarse en la carpeta donde se encuentra [Dockerfile](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/Dockerfile):

    sudo docker build -t bottelegraminfoactividadesugr ./

La segunda opción de instalación es hacerlo con el enlace a [Docker hub](https://hub.docker.com/r/antkk/bottelegraminfoactividadesugr/):

    sudo docker pull antkk/bottelegraminfoactividadesugr

Para ejecutar el bot primero accedemos al contenedor:

    sudo docker run -e "DATABASE_URL=XXX" -e "HOST_BD=XXX" -e "NAME_BD=XXX" -e "PW_BD=XXX" -e "TOKENBOT=XXX" -e "USER_BD=XXX" -i -t bottelegraminfoactividadesugr /bin/bash

Donde **XXX** hay que indicarle los valores de las variables de entorno para que se pueda conectar a la base de datos y el token de uso del bot de Telegram.

Para ejecutar el bot:

    cd BotTelegramInfoActividadesUGR/ActividadesUGRBot && python actividadesUGR_bot.py

La información completa de los pasos realizados para la creación, instalación y ejecución se encuentra aquí [enlace](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/Documentacion/documentacionhito4.md)

## Virtualización de Aplicaciones ##
El objetivo de este hito es crear y dar funcionalidad a una máquina virtual remota (IaaS), con la aplicación del proyecto, que en este caso es un bot de Telegram. Para el desarrollo del hito he usado:
- Azure: Proporciona un entorno gestionado para la ejecución y el despliegue de aplicaciones y servicios en la nube. Windows Azure proporciona a los desarrolladores un entorno de computación bajo demanda y almacenamiento alojado en los centros de datos de Microsoft para aplicaciones en la web.
- Vagrant: Vagrant es un software que nos permite construir nuestras máquinas virtuales de una forma rápida y automática a través del concepto que denominan "box" o caja. Para que Vagrant nos funcione necesitamos tener instalado VirtualBox.
- Fabric: permite empaquetar, implementar y administrar microservicios escalables y confiables.
- Ansible: Ansible es una herramienta que nos permite gestionar configuraciones, aprovisionamiento de recursos, despliegue automático de aplicaciones y muchas otras tareas de TI de una forma limpia y sencilla.
- Supervisor: gestor de procesos para ubuntu.

La información detallada de todos estos pasos lo podemos encontrar en [enlace documentación hito 5](http://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/Documentacion/documentacionhito5.md). En esta parte solo se indicará como realizar el proceso de despliegue y ejecución de la aplicación.

En este caso, todo el proceso es realmente sencillo ya que tenemos un archivo [**makefile**](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/makefile) con una serie de ordenes que nos sirve para poder realizar todo el despliegue sin necesidad de ir comando a comando instalando todo. El primer paso es desplegar la máquina virtual en azure, en este caso usamos:

    make despliegue

Se desplegará en Azure usando Vagrant. Para poder desplegar la máquina en azure, debemos de tener una cuenta con permisos de uso (vease documentación hito 5).

El siguiente paso es usar:

    make provision

Para provisionar la máquina virtual, se usa ansible que permite instalar una serie de paquetes definidos en el archivo **playbock.yml**. Si queremos añadir nuevos paquetes a la máquina virtual, no hará falta destruir dicha máquina, con utilizar make provision será suficiente.

Todos los demás comandos utilizan Fabric.
Si queremos descargar el contenido del repositorio que es donde está todo el contenido de la aplicación para poder ejecutarla, usamos:

    make install

Antes de ejecutar la aplicación podemos realizar los test con la orden:

    make test

De esta forma nos aseguramos de que la aplicación no contiene errores.
Para lanzar el bot utilizamos:

    make ejecutar

Si queremos pararlo:

    make parar
