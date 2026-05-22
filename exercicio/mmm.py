#!/bin/python3

import math
import os
import random
import re
import sys


while True:
    valor = input('Digite um valor [3] para saida a palavra (Weird): ')
    if valor not in ('3','Weird'):
        print('Digite um mnuemro correto')
        continue
    if valor == '3':
        print(valor)
        print('saindo do programa...')
        break
    elif valor == 'Weider':
        print('Weird')
        break
    else:
        print('Voce não dogitou nenhum valor valido.')
        continue
