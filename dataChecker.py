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
            texto = "\rProgreso: [{0}] {1}% {2}".format("#"*10, 100, 'Completado, parada por estancamiento\r\n')
            sys.stdout.write(texto)
            sys.stdout.flush()
            return True


def estadoEjecucion(iteraciones, total):
    progreso = 0
    estado = ""
    if iteraciones == 0:
        progreso = 0
        estado = "Iniciando..."
    elif iteraciones == (total - 1):
        progreso = 1
        estado = "Hecho, archivo de resultados finalizado.\r\n"
    else:
        progreso = float(iteraciones) / float(total)
    longBarra = 10
    bloque = int(round(longBarra*progreso))
    texto = "\rProgreso: [{0}] {1}% {2}".format("#"*bloque + "-"*(longBarra-bloque), progreso*100, estado)
    sys.stdout.write(texto)
    sys.stdout.flush()