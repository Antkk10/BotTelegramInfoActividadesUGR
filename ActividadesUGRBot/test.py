#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import funcionesdb

class TestStringMethods(unittest.TestCase):

    def test_hay_actividades(self):
        """ Test que comprueba si hay actividades disponibles. """
        total = funcionesdb.cantidadActividades()
        self.assertNotEqual(total, 0)

    def test_actividad_fecha(self):
        """ Test que devuelve true si hay actividades para una fecha concreta. """
        hay_actividades = funcionesdb.actividadesDisponibles("SELECT * FROM disponibles WHERE date='2017-01-01'")
        self.assertIsNotNONE(hay_actividades)

    def test_nombre_actividad(self):
        """ Test que devuelve true si el nombre de la actividad coincide"""
        nombre = funcionesdb.actividadesDisponibles("SELECT nombre FROM disponibles WHERE nombre='Charla Erasmus'")
        self.assertEqual(nombre, "Charla Erasmus")



if __name__ == '__main__':
   unittest.main()
