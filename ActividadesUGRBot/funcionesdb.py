#!/bin/usr/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

def nombreActividad(nombre):
    # Conectamos con mongo
    mongoClient = MongoClient('localhost', 27017)
    # Conectamos con la base de datos
    db = mongoClient['actividades_ugr']
    existe = ""

    #Obtenemos la consulta
    cursor = db['Actividades'].find({'actividad':nombre})
    if cursor.count() != 0:
        existe = True
    else:
        existe = False

    mongoClient.close()

    return existe

def actividadesDisponibles():
    # Conectamos con mongo
    mongoClient = MongoClient('localhost', 27017)
    # Conectamos con la base de datos
    db = mongoClient['actividades_ugr']

    # Obtenemos una colección para trabajar con ella
    cursor = db['Actividades'].find()

    resp = ""

    for c in cursor:
        resp += c['actividad'] + " " + c['fecha'] + " " + c['hora'] + '\n'

    mongoClient.close()
    return resp

def cantidadActividades():
    # Conectamos con mongo
    mongoClient = MongoClient('localhost', 27017)
    # Conectamos con la base de datos
    db = mongoClient['actividades_ugr']

    # Obtenemos una colección para trabajar con ella
    cursor = db['Actividades'].find()

    total = 0

    for c in cursor:
        total += 1

    mongoClient.close()
    return total
