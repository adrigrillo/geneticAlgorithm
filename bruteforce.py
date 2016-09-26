#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import urllib2
lst = list(itertools.product([0, 1], repeat=16))


# Esta funcion sera la que realice las peticiones html introduciendo el cromosoma como parametro


def getfitness(chromosome):
    petition = "http://163.117.164.230/age/?f=test&c=" + chromosome
    return urllib2.urlopen(petition).read()


# print getfitness(bina)'''


def add(x, y):
        maxlen = max(len(x), len(y))

        # Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry ! = 0:
            result = '1' + result

        return result.zfill(maxlen)
bina = '0000000000000000000000000000000000000000000000000000000000000000'
anterior = 0
aux = 0
bina_aux = '0'
fitness = 0
for i in range(0, (100000)):
        bina = add('1', bina)
        fitness = getfitness(bina)
        print (fitness)
        if anterior > fitness:
                aux = anterior
                bina_aux = bina
        else:
                anterior = fitness
print ("Fitness bueno =" + aux)
print ("Bina bueno =" + bina_aux)
