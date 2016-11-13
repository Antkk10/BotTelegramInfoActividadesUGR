#!/bin/usr/python
# -*- coding: utf-8 -*-

import psycopg2
import os
import urlparse

db = os.environ["NAME_BD"]
host_db = os.environ["HOST_BD"]
usuario = os.environ["USER_BD"]
pw = os.environ["PW_BD"]


def nombreActividad(consulta):

    con = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)

    cursor = con.cursor()
    cursor.execute(consulta)

    resp = ""
    filas = len(cursor.fetchall())

    con.close()

    if filas != 0:
        return True

    return False


def actividadesDisponibles():

    con = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
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


    con = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = con.cursor()
    cursor.execute('SELECT * FROM actividad')
    total = len(cursor.fetchall()) # Obtenemos el total
    con.close()
    return total
