#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
from tester import *
from decimal import *
import itertools
import random

# FUNCIÓN DEL TORNEO DE ELEMENTOS DE UNA POBLACIÓN, COGE A 4 AL AZAR DE poblacion, EVALUA AL MEJOR Y LO METE EN LA poblacionNueva


def torneo(poblacion):
    poblacionNueva = []
    jugadores = []
    for i in range(0, len(poblacion)):
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        ganador = evaluator(jugadores)
        poblacionNueva.append(ganador[0])
        del jugadores[:]
    return poblacionNueva
