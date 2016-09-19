#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2

# Esta funcion sera la que realice las peticiones html introduciendo el cromosoma como parametro


def getfitness(chromosome):
    petition = "http://163.117.164.230/age/?f=test&c=" + chromosome
    return urllib2.urlopen(petition).read()


bina = "0000000000000000000000000000000000000000000000000000000000000000"
print getfitness(bina)
