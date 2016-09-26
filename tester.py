#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
import urllib2

def getfitness(chromosome):
    petition = "http://163.117.164.230/age/?f=test&c=" + chromosome
    return urllib2.urlopen(petition).read()

def evaluator(poblacion):
    anterior = 0
    aux = 0
    bina_aux = '0'
    fitness = 0
    for i in range(0, len(poblacion)):
            fitness = getfitness(poblacion[i])
            print (fitness)
            if anterior > fitness:
                    aux = anterior
                    bina_aux = poblacion[i]
            else:
                    anterior = fitness
    return bina_aux, fitness

poblacion = generarPoblacion(100)
mejor = evaluator(poblacion)
print mejor
