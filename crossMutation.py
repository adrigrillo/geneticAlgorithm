#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


# ESTA FUNCION CRUZA (ALEATORIAMENTE) CROMOSOMA A CROMOSOMA LOS PADRES PARA FORMAR LA MISMA CANTIDAD DE DESCENDIENTES


def cruce(poblacion):
    i = 0
    poblacionNueva = []
    """ Reproducimos todos los individuos de la poblacion menos los dos últimos, que son los mejores
        de la anterior generación """
    while i < (len(poblacion) - 2):
        descendiente0 = ''
        descendiente1 = ''
        padre0 = poblacion[i]
        padre1 = poblacion[i + 1]
        for j in range(384):
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
    """ En este punto incluimos los dos mejores individuos de la población anterior """
    poblacionNueva.append(poblacion[i])
    poblacionNueva.append(poblacion[i + 1])
    return poblacionNueva


# ESTA FUNCION USA UN 0.1 DE PROBABILIDAD PARA MUTAR UN GEN DE LOS DESCENDIENTES


def mutacion(poblacion, tasaMutacion):
    poblacionNueva = []
    """ Al igual que en la reproduccion, mutamos todos los individuos de la poblacion menos los dos últimos,
        que son los mejores de la anterior generación """
    for i in range(len(poblacion) - 2):
        auxPoblacion = str(poblacion[i])
        for j in range(384):
            aux = random.randint(0, tasaMutacion)
            if aux == 0 and auxPoblacion[j] == '0':
                auxPoblacion = auxPoblacion[:j] + 'F' + auxPoblacion[j + 1:]
            elif aux == 0 and auxPoblacion[j] == 'F':
                auxPoblacion = auxPoblacion[:j] + '0' + auxPoblacion[j + 1:]
        poblacionNueva.append(auxPoblacion)
    """ En este punto incluimos los dos mejores individuos de la población anterior """
    poblacionNueva.append(poblacion[len(poblacion) - 2])
    poblacionNueva.append(poblacion[len(poblacion) - 1])
    return poblacionNueva
