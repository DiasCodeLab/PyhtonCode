
#========================
#Em desemvolvimento
#========================


arquivos = ['foto.png', 'senha.txt', 'python.py']

login = {
    'mateus':'123'
}

usuario = input('Digite um usuario: ')
senha = input('Digite uma senha')

usuario_aceito = usuario in login
senha_aceita = login[usuario] == senha

comando_cls = 'cls'
comando_dir = 'dir'
comando_logout = 'logout'

if usuario_aceito and senha_aceita:
    print('='*20)
    print('C:\Users\Mateus>')
    print('='*20)
    comandos = input(': ')
    if comandos == comando_cls:
            print('='*20)
            print('')
            print('='*20)
    elif comandos == comando_dir:
          print(arquivos)
...          


