#!/usr/bin/env python
# -*- coding: utf-8 -*-


def saveData(nomFichero, iteracion, tiempoIteracion, fitness):
    file = open(nomFichero, 'a')
    data = str(iteracion) + ',' + str(tiempoIteracion) + ',' + str(fitness)
    file.write(data + '\n')
    file.close()

