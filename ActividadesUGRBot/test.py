#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import funcionesdb

""" Los test que realicé para el hito 2. Para el hito 3 he cambiado la base de datos y tenemos los test abajo."""
#class TestStringMethods(unittest.TestCase):

#    def test_hay_actividades(self):
        #""" Test que comprueba si hay actividades disponibles. """
#        total = funcionesdb.cantidadActividades()
#        self.assertNotEqual(total, 0)

#    def test_actividad_fecha(self):
        #""" Test que devuelve true si hay actividades para una fecha concreta. """
#        hay_actividades = funcionesdb.actividadesDisponibles("SELECT * FROM disponibles WHERE fecha='2017-01-01'")
#        self.assertIsNotNone(hay_actividades)

#    def test_nombre_actividad(self):
        #""" Test que devuelve true si el nombre de la actividad coincide"""
#        nombre = funcionesdb.actividadesDisponibles("SELECT nombre FROM disponibles WHERE nombre='Charla Erasmus'")
#        self.assertEqual(nombre, "Charla Erasmus\n")

class TestStringMethods(unittest.TestCase):

    def test_hay_actividades(self):
        """ Test que comprueba si hay actividades disponibles. """
        total = funcionesdb.cantidadActividades()
        self.assertNotEqual(total, 0)

    def test_nombre_actividad(self):
        """ Test que devuelve true si el nombre de la actividad coincide"""
        existe = funcionesdb.nombreActividad("Charla python")
        self.assertTrue(existe)

if __name__ == '__main__':
   unittest.main()
