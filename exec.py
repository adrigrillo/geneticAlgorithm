#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from main import *

""" Esta clase será utilizada para hacer las correspondientes llamadas al algoritmo
    para ello se llamara a la funcion main de la siguiente forma:
    main(tamanoPoblacion = (valor), numGeneraciones = (valor), tasaMutacion = (valor), partipantesTorneo = (valor),
         parada = (True/False))"""
main(tamanoPoblacion = 10, numGeneraciones = 500, tasaMutacion = 100, partipantesTorneo = 2, parada = True)
