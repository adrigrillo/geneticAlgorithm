#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


fitnessIter = []


def saveData(nomFichero, iteracion, tiempoIteracion, fitness):
    """
    Funcion que guarda los datos de la partida en cada iteracion
    :param nomFichero: Nombre del fichero donde se guardaran los datos.
    :param iteracion: Numero de iteracion en la que se encuentra el programa.
    :param tiempoIteracion: Tiempo que ha tardado en ejecutarse la iteracion.
    :param fitness: Resultado de la evaluación sobre el mejor individuo de la población.
    :return:
    """
    file = open(nomFichero, 'a')
    data = str(iteracion) + ';' + str(tiempoIteracion) + ';' + str(fitness)
    file.write(data + '\n')
    file.close()


def paradaAlgoritmo(iteracion, fitness):
    """
    Funcion que comprueba el fitness a 10 ejecuciones e interrumpe la ejecución del algoritmo si es igual
     fitness de la iteracion actual.
    :param iteracion: numero de la iteracion actual
    :param fitness: fitness de la iteracion actual
    :return:
    """
    fitnessIter.append(fitness)
    if iteracion >= 10:
        if fitnessIter.pop(0) == fitness:
            sys.exit("Realizado, parada por estancamiento")


def estadoEjecucion(iteraciones, total):
    progreso = iteraciones / total
    barLength = 10
    estado = ""
    if isinstance(progreso, int):
        progreso = float(progreso)
    if progreso < 0:
        progreso = 0
        estado = "Iniciando...\r\n"
    if progreso >= 1:
        progreso = 1
        estado = "Hecho, archivo de resultados finalizado.\r\n"
    block = int(round(barLength*progreso))
    text = "\rProgreso: [{0}] {1}% {2}".format("#"*block + "-"*(barLength-block), progreso*100, estado)
    sys.stdout.write(text)
    sys.stdout.flush()