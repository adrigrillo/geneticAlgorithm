#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tester import *
import random

""" FUNCIÓN DEL TORNEO DE ELEMENTOS DE UNA POBLACIÓN, COGE A 4 AL AZAR DE poblacion,
    EVALUA AL MEJOR Y LO METE EN LA poblacionNueva """


def torneo(poblacion):
    poblacionNueva = []
    jugadores = []
    """ Aqui guardamos el mejor de la poblacion anterior (elitismo) """
    poblacionNueva.append(evaluator(poblacion)[0])
    for i in range(len(poblacion)-1):
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        ganador = evaluator(jugadores)
        poblacionNueva.append(ganador[0])
        del jugadores[:]
    return poblacionNueva
