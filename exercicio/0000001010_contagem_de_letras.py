frase = "Quem aprende a dominar a própria mente, domina qualquer desafio que a vida colocar no caminho."


while True:

    try:

        menu = input( 'Deseja continuar ? [S]sim [N]não: ').lower()

        if  menu  not in ('s','n'):
            print('Voce não digitou uma letra...')
            continue
        
        if menu == 'n':
            print('Volte sempre...')
            break

        letra = input('Digite a letra que deseja procurar: ')

        frase_lower = frase.lower() 

        if letra in frase_lower: 
            contagem = frase_lower.count(letra)
            print(f"foi identificasdo a letra: ({letra}) e ela se repete {contagem} vezes!")
            continue    
        else :
            print(f'A frase não possui a letra {letra}')
            continue

    except TypeError:
       print('Erro, tente novamente...')
