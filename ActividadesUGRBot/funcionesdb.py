#!/bin/usr/python
# -*- coding: utf-8 -*-

import sqlite3

def actividadesDisponibles(consulta):
    db = sqlite3.connect('actividades.db') # conectamos con la bd
    b = db.cursor()
    b.execute(consulta) # Obtenemos el resultado de la consulta
    resp = ""
    for r in b:
        # Mandamos un string con un formato válido.
        aux = str(r)
        pos1 = aux.find("'")
        pos2 = aux.find("'", len(aux)-3)
        final = ""
        for i in range(pos1+1, pos2):
            final += aux[i]
        resp += str(final) + "\n"

    # Cierre de conexión con la base de datos.
    b.close()
    db.close()
    return resp

def cantidadActividades():
    """ Función que devuelve el total de actividades disponibles """
    # Conectamos con la base de datos
    db = sqlite3.connect('actividades.db')
    b = db.cursor()
    b.execute("SELECT * FROM disponibles") # Obtenemos el resultado de la consulta
    total = len(b) # Obtenemos la cantidad total de actividades disponibles
    # Cerramos la base de datos
    b.close()
    db.close()
    return total

def insertar(nombre, fecha, hora):
    db = sqlite3.connect('actividades.db')
    b = db.cursor()
    b.execute("INSERT INTO disponibles (nombre, fecha, hora) VALUES (?, ?, ?)", (nombre, fecha, hora))
    db.commit()
    b.close()
    db.close()
