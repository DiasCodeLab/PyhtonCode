import random

tentativas = 5

lista = ['mateus', 'dias', 'onça', 'leao']

sortear_nome = random.choice(lista)

tracos = ['_'] * len(sortear_nome)

while tentativas > 0:

    print(' '.join(tracos))

    digito = input('Digite uma letra: ').lower()

    acertou = False

    for i in range(len(sortear_nome)):

        if sortear_nome[i] == digito:
            tracos[i] = digito
            acertou = True

    if not acertou:
        tentativas -= 1
        print(f'Você errou! Restam {tentativas} tentativas.')

    if '_' not in tracos:
        print('Você ganhou!')
        print(f'A palavra era: {sortear_nome}')
        break