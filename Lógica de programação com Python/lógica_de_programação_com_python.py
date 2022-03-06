## Lógica de programação com Python

1+1

"Raphael"

'Raphael'

nome='Raphael'

nome

idade=34

idade

nome

idade

print(f'O nome é {nome} e sua idade é {idade} anos')

idade = 35

print(f'O nome é {nome} e sua idade é {idade} anos')



"""## Criando minha primeira função"""

def saudacao():
  nome = input('Qual o seu nome? ')
  print (f'Olá {nome}')

saudacao()

"""## Parâmetros"""

nome = 'João'

def saudacao_com_parametro(nome_da_pessoa):
  print(f'Olá {nome_da_pessoa}')

saudacao_com_parametro(nome)

"""## Condicional"""

idade = 10

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

verifica_se_pode_dirigir(idade)

"""## Convertendo tipo para inteiro"""

def verifica_se_pode_dirigir_sem_parametros():
  idade = input('Qual sua idade? ')
  idade = int(idade)
  if idade >= 18:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

verifica_se_pode_dirigir_sem_parametros()

"""## Lista"""

idade = 22
idade

type(idade)

nome = 'Raphael'
type(nome)

idades = [18,22,15,50]
type(idades)

idades[2]

idades = [18,22,15,50]
#          0  1  2  3 
#          0 -3 -2 -1

idades[1]

idades[0:3]

idades[1:]

idades[-1]

idades[-2]

"""## Laços e loops"""

idades

# for fora da função

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print(f'{idade} anos de idade, TEM permissão para dirigir')
  else:
    print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')

# para cada idade em nossa lista:
  # verifica_se_pode_dirigir(idade)

for idade in idades:
  verifica_se_pode_dirigir(idade)

# for dentro da função

def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
      print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')
verifica_se_pode_dirigir(idades)

"""## Booleano"""

idade = 18
idade >= 18

idade = 15
idade >= 18

permissoes = []
idades = [20,14,40]

def verifica_se_pode_dirigir(idades,permissoes):
  for idade in idades:
    if idade >= 18:
      permissoes.append(True)
    else:
      permissoes.append(False)

verifica_se_pode_dirigir(idades,permissoes)

permissoes

for permissao in permissoes:
  if permissao == True:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

"""## Tipos em uma lista"""

lista = ['Raphael', 34, True, '25']

for elemento in lista:
  print(f'O elemento {elemento} é do tipo: ', type(elemento))

"""## Import"""

from random import randrange, seed

seed(11)

randrange(0,11)

notas_matematica = []

for notas in range(8):
  notas_matematica.append(randrange(0,11))

notas_matematica

len(notas_matematica)

"""## Matplotlib"""

import matplotlib.pyplot as plt

x = list(range(1,9))
y = notas_matematica
plt.plot(x,y,marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()

notas_matematica

import matplotlib.pyplot as plt

notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
notas_portugues = ['Português',9,9,9,8,5,6,8,5]
notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]

notas = [notas_matematica, notas_portugues, notas_geografia]

for nota in notas:
 x = list(range(1, 9))
 y = nota[1:]
 plt.plot(x, y, marker='o')
 plt.xlabel('Provas')
 plt.ylabel('Notas')
 plt.title(nota[0])
 plt.show()

