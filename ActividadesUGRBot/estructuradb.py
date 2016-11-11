# -*- coding: utf-8 -*-

class Actividades:
    """Contiene las actividades de la semana de la
       etsiit. """

    def __init__(self, actividad, fecha, hora):
        """Constructor de clase que inicializa los
        atributos. """
        self.actividad = actividad
        self.fecha = fecha
        self.hora = hora


    def ColeccionDB(self):
        return {
            "actividad": self.actividad,
            "fecha": self.fecha,
            "hora": self.hora
            }


    def __str__(self):
        return "Actividad: %s Fecha: %s Hora: %s" \
                %(self.actividad, self.fecha, self,hora)
