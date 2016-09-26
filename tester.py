#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generator import *
import urllib2

def getfitness(chromosome):
    petition = "http://163.117.164.230/age/?f=test&c=" + chromosome
    return urllib2.urlopen(petition).read()

def evaluator(poblacion):
    aux = 1000000
    bina_aux = '0'
    fitness = 0
    for i in range(0, len(poblacion)):
            fitness = getfitness(poblacion[i])
            print ("aux " + str(aux) + " fitness = " + str(fitness))
            if aux > fitness:
                    print("hola")
                    aux = fitness
                    bina_aux = poblacion[i]
    return bina_aux, aux

poblacion = generarPoblacion(100)
mejor = evaluator(poblacion)
print mejor
