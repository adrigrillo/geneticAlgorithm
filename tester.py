#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from decimal import *


# FUNCIÓN DE PETICIÓN DE EVALUACIÓN A LA PÁGINA OFRECIDA POR EL ENUNCIADO DE LA PRÁCTICA


def getfitness(chromosome):
    petition = "http://163.117.164.219/age/alfa?c=" + chromosome
    return urllib2.urlopen(petition).read()

# FUNCIÓN DE EVALUACIÓN, RECOGE A poblacion Y BUSCA EL MEJOR CON LA AYUDA DE getfitness


def evaluator(poblacion):
    aux = getfitness(poblacion[0])
    bina_aux = poblacion[0]
    fitness = 0
    for i in range(0, len(poblacion)):
        fitness = getfitness(poblacion[i])
        if (Decimal(fitness) < Decimal(aux)):
            aux = fitness
            bina_aux = poblacion[i]
    return bina_aux, aux
