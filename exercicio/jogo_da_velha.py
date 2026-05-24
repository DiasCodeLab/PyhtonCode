import random

lista = ['oi', 'ola', 'tudo bem']

nova_lista = lista[:]  # copia
random.shuffle(nova_lista)

print("Original:", lista)
print("Embaralhada:", nova_lista)