#!/bin/env/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

con = psycopg2.connect(database='actividades')

cursor = con.cursor()

cursor.execute("CREATE TABLE actividad(ID INTEGER PRIMARY KEY, nombre VARCHAR(30) NOT NULL, fecha VARCHAR(20) NOT NULL, hora VARCHAR(20) NOT NULL)")
cursor.execute("INSERT INTO actividad(ID, nombre, fecha, hora) VALUES(1, 'Charla python', '17/07/2018', '20:00')")
cursor.execute("INSERT INTO actividad(ID, nombre, fecha, hora) VALUES(2, 'Charla Java', '20/07/2018', '10:00')")
cursor.execute("INSERT INTO actividad(ID, nombre, fecha, hora) VALUES(3, 'Charla C', '20/07/2018', '10:00')")

con.commit()

con.close()
