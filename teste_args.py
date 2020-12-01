

import argparse

parser = argparse.ArgumentParser(description = 'Entra com o nome do usuario', add_help = False)
parser = argparse.ArgumentParser()

parser.add_argument('-i','--nome', action='store',
    dest='name', required = True, nargs='+',
    help = "Os nomes dos usuarios")

argumentos = parser.parse_args()

lista_nomes = argumentos.name[0].split(",")

from random import randint
dict_list = []
for i in lista_nomes:
	key = randint(1,1000)
	dict_list.append([str(key),i])

dicionario = dict(dict_list)
print(dicionario)

