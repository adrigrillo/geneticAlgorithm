#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from generator import *
from tournament import *
from crossMutation import *
import time

# COSAS A ARREGLAR, MIRAR EL PORQUÉ DE LA PARADA EN LA ITERACION 51, Y ESTUDIAR A PARTIR DE LA ITERACIÓN 16 DEJA DE OPTIMIZAR


def main():
    start = time.time()
    contador = 1
    print contador
    poblacion = generarPoblacion(100)
    mejor = evaluator(poblacion)
    print mejor
    nuevaPoblacion = torneo(poblacion)
    nuevaPoblacion = cruce(nuevaPoblacion)
    stop = time.time()
    print(stop - start)
    for i in range(0, 999):
        start = time.time()
        contador = contador + 1
        print contador
        mejor = evaluator(nuevaPoblacion)
        print mejor
        nuevaPoblacion = torneo(nuevaPoblacion)
        nuevaPoblacion = cruce(nuevaPoblacion)
        stop = time.time()
        print(stop - start)

    print mejor

main()
