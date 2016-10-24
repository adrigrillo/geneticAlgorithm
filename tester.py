#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from decimal import *


llamadas = 0


def getfitness(chromosome):
    """
    FUNCIÓN DE PETICIÓN DE EVALUACIÓN A LA PÁGINA OFRECIDA POR EL ENUNCIADO DE LA PRÁCTICA
    :param chromosome: Cromosoma a analizar
    :return:
    """
    global llamadas
    petition = "http://163.117.164.219/age/alfa?c=" + ''.join(chromosome)
    llamadas += 1
    return urllib2.urlopen(petition).read()


def evaluator(poblacion):
    """
    FUNCIÓN DE EVALUACIÓN, RECOGE A poblacion Y BUSCA EL MEJOR CON LA AYUDA DE getfitness
    :param poblacion: Poblacion a analizar
    :return:
    """
    aux = getfitness(poblacion[0])
    bina_aux = poblacion[0]
    for i in range(len(poblacion)):
        fitness = getfitness(poblacion[i])
        if Decimal(fitness) < Decimal(aux):
            aux = fitness
            bina_aux = poblacion[i]
    return bina_aux, aux


def devolverllamadas():
    """
    Devuelve el numero de llamadas realizadas
    :return:
    """
    global llamadas
    return llamadas


def reiniciarllamadas():
    """
    Reinicia el numero de llamadas realizadas al servidor, al reiniciar la ejecucion
    :return:
    """
    global llamadas
    llamadas = 0