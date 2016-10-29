# coding: utf-8

import telebot

# token que nos dio bot father
token = "285555767:AAGH4tCGG2Q2Qx_uhJFYEDhIVWx_TRhSfCI"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['hola', 'start'])
def enviar_bienvenida(message):
    """Función de bienvenida del canal. """
    bot.reply_to(message, "Bievenid@ al canal de actividades de la UGR")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
