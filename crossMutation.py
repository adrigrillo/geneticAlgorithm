#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


# ESTA FUNCION CRUZA (ALEATORIAMENTE) CROMOSOMA A CROMOSOMA LOS PADRES PARA FORMAR LA MISMA CANTIDAD DE DESCENDIENTES


def cruce(poblacion):
    print "Longitud de la poblacion antes de reproducir ", len(poblacion)
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
        i = i + 2
    print "Longitud de la poblacion nueva ", len(poblacionNueva)
    return poblacionNueva


# ESTA FUNCION USA UN 0.1 DE PROBABILIDAD PARA MUTAR UN GEN DE LOS DESCENDIENTES


def mutacion(poblacion):
    for i in range(0, len(poblacion)):
        for j in range(0, 64):
            aux = random.randint(0, 10)
            if (aux == 0 and poblacion[i][j] == 0):
                poblacion[i][j] = 1
            elif (aux == 0 and poblacion[i][j] == 1):
                poblacion[i][j] = 0
    return poblacion
