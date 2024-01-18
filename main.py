# testando requisiçõe html

import requests

# criando um limpador de tela para o terminal
from os import system as cmd
cls  = lambda: cmd('cls') or None

# executando o limpador de tela no inicio do codigo
cls()


url = 'http://google.com/'


response = requests.get(url)


print(f'Estatus: {response.status_code}, Requisição de: {response.url}')
print()
print()

print('- CABEÇALHO')
for i in response.headers:
    print(i)
print()


print(f'- COOKIES:')
for i in response.cookies:
    print(i)
print()

