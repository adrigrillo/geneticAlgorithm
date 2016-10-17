#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tester import *
import random

""" FUNCIÓN DEL TORNEO DE ELEMENTOS DE UNA POBLACIÓN, COGE A 4 AL AZAR DE poblacion,
    EVALUA AL MEJOR Y LO METE EN LA poblacionNueva """


def torneo(poblacion):
    poblacionNueva = []
    jugadores = []
    """ Realizamos torneos de 4 individuos al azar, el numero de torneos sera el del tamaño de la poblacion
        menos dos para conseguir 98 individuos y posteriormente guardar los dos mejores de la poblacion """
    for i in range(len(poblacion) - 2):
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        ganador = evaluator(jugadores)
        poblacionNueva.append(ganador[0])
        del jugadores[:]
    """ Tras hacer el torneo, vamos a coger los dos mejores individuos de la población """
    elite = evaluator(poblacion)[0]
    poblacionNueva.append(elite)
    poblacion.remove(elite)
    elite = evaluator(poblacion)[0]
    poblacionNueva.append(elite)
    return poblacionNueva
