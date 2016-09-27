#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import random

# CREADOR DE POBLACIONES, DEVUELVE UNA LISTA FORMADA POR numIndividuos ELEMENTOS DE CONCATENACIONES DE 4 CADENAS BINARIAS DE 16 BITS ALEATORIAS


def generarPoblacion(numIndividuos):
    lst = list(itertools.product([0, 1], repeat=16))
    generador = []
    for i in range(0, numIndividuos):
        generador.append(lst[random.randint(0, pow(2, 16) - 1)] + lst[random.randint(0, pow(2, 16) - 1)] + lst[random.randint(0, pow(2, 16) - 1)] + lst[random.randint(0, pow(2, 16) - 1)])
    poblacion = []
    for i in range(0, numIndividuos):
        cromosoma = ""
        for j in range(0, 64):
            cromosoma += str(generador[i][j])
        poblacion.append(cromosoma)
    return poblacion