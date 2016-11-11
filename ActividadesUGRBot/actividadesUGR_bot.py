# -*- coding: utf-8 -*-

import telebot # librería para usar el bot
import sqlite3 # Para usar la base de datos sqlite3
#from funcionesdb import actividadesDisponibles # Función para hacer peticiones
import funcionesdb
from pymongo import MongoClient

# token que nos dio bot father
token = "285555767:AAGH4tCGG2Q2Qx_uhJFYEDhIVWx_TRhSfCI"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['hola', 'start'])
def enviar_bienvenida(message):
    """Función de bienvenida del canal. """
    bot.reply_to(message, "Bievenid@ al canal de actividades de la UGR")

@bot.message_handler(commands=['actividades'])
def enviar_actividades(m):
    """Función que envia las actividades de la semana al usuario. """
    cid = m.chat.id # Obtenemos la id del usuario.
    resp = funcionesdb.actividadesDisponibles()
    bot.send_message(cid, resp)

@bot.message_handler(commands=['cantidad_actividades'])
def cantidad_actividades(m):
    """ Función que envia la cantidad de actividades disponibles. """
    cid = m.chat.id # obtenemos la id del usuario
    total = funcionesdb.cantidadActividades()
    bot.send_message(cid, total)

#@bot.message_handler(commands=['fecha'])
#def enviar_fecha(m):
#    """ Función que envia al usuario las actividades y fechas disponibles. """
#    cid = m.chat.id # Obtenemos la id del usuario.
#    resp = actividadesDisponibles()
#    bot.send_message(cid, resp)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True) # Le indicamos que nunca termine de funcionar.
