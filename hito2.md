
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
