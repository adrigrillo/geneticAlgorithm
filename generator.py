#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def generarPoblacion(numIndividuos):
    """
    CREADOR DE POBLACIONES, DEVUELVE UNA LISTA FORMADA POR numIndividuos INDIVIDUOS, ESTOS ESTAN FORMADOS POR 384
    BITS QUE REPRESENTAN 24 ESTACIONES DE 16 SENSORES
    :param numIndividuos: Numero de individuos que tendra la poblacion
    :return:
    """
    sensores = ['0', 'F', 'H']
    poblacion = []
    for i in range(numIndividuos):
        individuo = []
        for j in range(384):
            individuo.append(random.choice(sensores))
        poblacion.append(individuo)
    return poblacion
