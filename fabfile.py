# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def InstalaAplicacion():
    """ Función para descargar el bot del repositorio. """

    # Descargamos la app
    run('git clone https://github.com/Antkk10/BotTelegramInfoActividadesUGR.git')

    # Accedemos y terminamos de instalar los requisitos
    run('cd BotTelegramInfoActividadesUGR/ && pip install -r requirements.txt')

def EjecutarApp():
    """ Función para ejecutar el Bot. """
    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PW_BD=os.environ['PW_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                    ):
        run('sudo supervisorctl start botactividades')

def StopApp():
    """ Función que para el bot. """
    run('sudo supervisorctl stop botactividades')

def TestApp():
    with shell_env(HOST_BD=os.environ['HOST_BD'],
                    USER_BD=os.environ['USER_BD'],
                    PW_BD=os.environ['PW_BD'],
                    NAME_BD=os.environ['NAME_BD'],
                    TOKENBOT=os.environ['TOKENBOT']
                    ):
        run('cd BotTelegramInfoActividadesUGR/ActividadesUGRBot && python test.py')
