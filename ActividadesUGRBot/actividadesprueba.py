#!/bin/env/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from estructuradb import Actividades

# Lista de actividades actuales
actividades = [
    Actividades('Charla python', '20/10/2017', '20:00'),
    Actividades('Charla Java', '21/11/2018', '17:00')
]

# Conectamos con mongo
mongoClient = MongoClient('localhost', 27017)

# Conectamos con la base de datos
db = mongoClient['actividades_ugr']

# Obtenemos una colección para trabajar con ella
coleccion = db['Actividades']
# Insertamos los datos
for act in actividades:

    coleccion.insert(act.ColeccionDB())


mongoClient.close() # Cerramos la base de datos
