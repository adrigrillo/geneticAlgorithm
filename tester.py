#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
import urllib2
from decimal import *


def getfitness(chromosome):
    petition = "http://163.117.164.230/age/?f=test&c=" + chromosome
    return urllib2.urlopen(petition).read()


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
