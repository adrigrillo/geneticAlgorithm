#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
from tester import *
from decimal import *
import itertools
import random

poblacionNueva = []
jugadores = []


def torneo(poblacion):
    for i in range(0, len(poblacion)):
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        jugadores.append(poblacion[random.randint(0, len(poblacion) - 1)])
        ganador = evaluator(jugadores)
        poblacionNueva.append(ganador[0])
        del jugadores[:]
    return poblacionNueva

poblacionTorneo = generarPoblacion(100)
print torneo(poblacionTorneo)
