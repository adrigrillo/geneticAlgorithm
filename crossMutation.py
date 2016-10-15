#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
import random
import sys


# ESTA FUNCION CRUZA (ALEATORIAMENTE) CROMOSOMA A CROMOSOMA LOS PADRES PARA FORMAR LA MISMA CANTIDAD DE DESCENDIENTES


def cruce(poblacion):
    i = 0
    poblacionNueva = []
    while (i < len(poblacion)):
        descendiente0 = ''
        descendiente1 = ''
        padre0 = poblacion[i]
        padre1 = poblacion[i + 1]
        for j in range(0, 64):
            aux = random.randint(0, 1)
            if aux == 0:
                descendiente0 = descendiente0 + padre0[j]
                descendiente1 = descendiente1 + padre1[j]
            else:
                descendiente0 = descendiente0 + padre1[j]
                descendiente1 = descendiente1 + padre1[j]
        poblacionNueva.append(descendiente0)
        poblacionNueva.append(descendiente1)
        i += 2
    return poblacionNueva


# ESTA FUNCION USA UN 0.1 DE PROBABILIDAD PARA MUTAR UN GEN DE LOS DESCENDIENTES


def mutacion(poblacion):
    poblacionNueva = []
    for i in range(0, len(poblacion)):
        auxPoblacion = str(poblacion[i])
        for j in range(0, 64):
            aux = random.randint(0, 100)
            if (aux == 0 and auxPoblacion[j] == '0'):
                auxPoblacion = auxPoblacion[:j] + '1' + auxPoblacion[j + 1:]
            elif (aux == 0 and auxPoblacion[j] == '1'):
                auxPoblacion = auxPoblacion[:j] + '0' + auxPoblacion[j + 1:]
        poblacionNueva.append(auxPoblacion)
    return poblacionNueva
