#!/usr/bin/env python
# -*- coding: utf-8 -*-


def saveData(nomFichero, iteracion, tiempoIteracion, fitness):
    file = open(nomFichero, 'a')
    data = iteracion + ',' + tiempoIteracion + ',' + fitness

