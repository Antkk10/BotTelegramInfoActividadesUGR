

# proyectoIV

La descripción del proyecto se encuentra en la rama master del repositorio.

### Explicación del uso de las herramientas escogidas para el desarrollo del proyecto ###

1. El bot está en la nube para que los usuarios tengan siempre acceso a la información que ofrece el bot.
2. Docker: automatiza el despliegue de aplicaciones dentro de contenedores de software. Lo voy a utilizar porque ha sido comentado en clase y no conozco otro.
3. Uso de Telegram para que los usuarios puedan obtener información de actividades d ela universidad. La aplicación de Telegram es accesible a todo el mundo y muy usada para chatear entre otras tareas.
4. Para el desarrollo del bot voy a usar el lenguaje de programación Python. Es una de las opciones que se pueden usar y quiero aprender a programar en este lenguaje.
5. En el proyecto uso almacenes de datos para separar la información. Juan ha explicado en clase que es muy importante tener varias base de datos y que cada una maneja la información que le corresponde (explicada en README.md). Sobre que base de datos usar para cada una de las tres opciones, se está valorando.


## Documentación correspondiente a todo el desarrollo del hito 2 ##

### Travis ###
**Travis** es un sistema distribuido de integración continua libre integrado en Github.

Para obtener una cuenta en [Travis](https://travis-ci.org/) la he asociado a mi cuenta de Github ya que
Travis lo permite.
Una vez que he asociado mi cuenta de Github a Travis, he insertado el repositorio para realizar los test.
Eso se hace pulsando en la pestaña accounts en la esquina superior derecha que aparece al pasar el puntero del ratón
sobre el nuestro nombre. Al pulsar aparece todos los repositorios que tiene nuestra cuenta y debemos de seleccionar
la cuenta en la que queramos que se hacen los test.

Después de la configuración debemos subir un archivo .travis.yml con el contenido de configuración de la maquina virtual
que hará los test. El archivo que yo he subido es el siguiente: [archivo](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/.travis.yml).

Por último, el icono que aparece en el [README](https://github.com/Antkk10/BotTelegramInfoActividadesUGR/blob/master/README.md) si pulsamos encima de el nos lleva a la página de Travis donde se testea que todo funciona correctamente. Para insertar el código nos vamos a la página de [Travis](https://travis-ci.org/) (con el repositorio ya asociado a la cuenta) pulsamos encima del icono de build (está al lado del icono de github y en la misma linea que el nombre del repositorio) y seleccionamos Branch --> Master, Segunda Linea --> Markdown y copiamos todo el contenido que aparece en el tercer bloque. Eso que hemos copiado lo insertamos en el README.md del repositorio y ya tenemos el icono en nuestro repositorio.

### Información. ###
Para desarrollar el hito 2, he obtenido la información para el desarrollo del bot de [](https://docs.python.org/2/) y [](https://github.com/eternnoir/pyTelegramBotAPI)
