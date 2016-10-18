#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from generator import *
from tournament import *
from crossMutation import *
from dataChecker import *
import time


def main(tamanoPoblacion, numGeneraciones, tasaMutacion, partipantesTorneo):
    """
    Version de cromosomas con 384 bits que soportan el vocabulario '0' y 'F'
    :param tamanoPoblacion: Sera el tamaño de la poblacion deseada
    :param numGeneraciones: El número de generaciones que queremos crear, es decir, las veces que se ejecutará el ciclo
    :param tasaMutacion: Tasa de mutacion de los cromosomas. Sera de 1 sobre el valor establecido
    :param partipantesTorneo: Numero de individuos que participara en cada ronda del torneo
    :return: Imprime fichero con los resultados de la ejecución
    """
    """ Creamos el nombre de fichero para esta ejecucion y la poblacion """
    nomFichero = 'salidas' + time.strftime("%d-%H%M%S") + '.txt'
    poblacion = generarPoblacion(tamanoPoblacion)
    """ Empezamos con el proceso """
    for i in range(numGeneraciones):
        start = time.time()
        mejor = evaluator(poblacion)
        poblacion = torneo(poblacion, partipantesTorneo)
        poblacion = cruce(poblacion)
        poblacion = mutacion(poblacion, tasaMutacion)
        stop = time.time()
        saveData(nomFichero, i, (stop - start), mejor[1])
        if paradaAlgoritmo(i, mejor[1]) is True:
            break
        estadoEjecucion(i, numGeneraciones)
