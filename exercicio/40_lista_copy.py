
lista = ['',1,True,'false']

#aqui é feita o copia da lista em lista2 onde ao mecher na lista 2 não interfere na lista
lista2 = lista.copy()

lista3 = lista

print(lista)
print(lista2)


# neste caso ao alterar a lista3 ela altera a lista 1 
print(lista3)