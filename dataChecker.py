#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

""" Arrays donde se almacenaran los resultados de la funcion de evaluacion """
fitnessIterAnteriores = []
fitnessIterActuales = []
iterAtascado = 0


def saveData(nomFichero, iteracion, tiempoIteracion, fitness, tamanoPoblacion, tasaMutacion, participantesTorneo):
    """
    Funcion que guarda los datos de la partida en cada iteracion
    :param nomFichero: Nombre del fichero donde se guardaran los datos.
    :param iteracion: Numero de iteracion en la que se encuentra el programa.
    :param tiempoIteracion: Tiempo que ha tardado en ejecutarse la iteracion.
    :param fitness: Resultado de la evaluación sobre el mejor individuo de la poblacion.
    :param tamanoPoblacion: Tamaño de la poblacion para la ejecucion
    :param tasaMutacion: Tasa de mutacion para la ejecucion
    :param participantesTorneo: numero de participantes en los torneos de la ejecucion
    :return:
    """
    file = open(nomFichero, 'a')
    if iteracion is 0:
        file.write('Ejecucion con tamaño de poblacion ' + str(tamanoPoblacion) + ', con tasa de mutacion del ' +
                   str(float(1) / float(tasaMutacion)) + '%, y con torneos de ' + str(participantesTorneo) + '\n')
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
    global iterAtascado, fitnessIterActuales, fitnessIterAnteriores
    if iteracion < 30:
        """ Metemos los valores actuales durante las x primeras iteraciones en la lista que tendra los antiguos """
        fitnessIterAnteriores.append(fitness)
    elif iteracion >= 30:
        """ Metemos los valores actuales a partir de las x iteraciones en la lista que tendra los nuevos """
        fitnessIterActuales.append(fitness)
        if iteracion >= 40:
            """ A partir de las x iteraciones, los actuales se meten en la nueva lista, pero se cede el ultimo a la
                lista vieja para ir asi actualizando los valores en ambas listas """
            fitnessIterAnteriores.pop(0)
            fitnessIterAnteriores.append(fitnessIterActuales.pop(0))
            if min(fitnessIterAnteriores) <= min(fitnessIterActuales):
                """ Si el minimo de la lista vieja es menor o igual al menor de la nueva durante tres iteraciones se
                    produce parada por estancamiento """
                iterAtascado += 1
                """ Si se produce un estacamiento durante más de 5 turnos se toma como estancamiento """
                if iterAtascado == 5:
                    texto = "\rProgreso: [{0}] {1}% {2}".format("#"*10, 100, 'Completado, parada por estancamiento\r\n')
                    sys.stdout.write(texto)
                    sys.stdout.flush()
                    return True


def estadoEjecucion(iteraciones, total):
    progreso = 0
    estado = "Completado. Ejecutando..."
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
