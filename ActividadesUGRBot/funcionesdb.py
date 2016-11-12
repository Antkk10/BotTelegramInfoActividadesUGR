#!/bin/usr/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def nombreActividad(consulta):

    con = psycopg2.connect(database='actividades', host=url.hostname, port.url.port)

    cursor = con.cursor()
    cursor.execute(consulta)

    resp = ""
    filas = len(cursor.fetchall())

    con.close()

    if filas != 0:
        return True

    return False


def actividadesDisponibles():

con = psycopg2.connect(database='actividades', host=url.hostname, port.url.port)
    cursor = con.cursor()
    cursor.execute('SELECT * FROM actividad')

    resp = ""
    filas = cursor.fetchall()
    for c in filas:
        # Almacena el nombre de la actividad, fecha y hora
        resp += str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + "\n"
    con.close()

    return resp

def cantidadActividades():


con = psycopg2.connect(database='actividades', host=url.hostname, port.url.port)
    cursor = con.cursor()
    cursor.execute('SELECT * FROM actividad')
    total = len(cursor.fetchall()) # Obtenemos el total
    con.close()
    return total
