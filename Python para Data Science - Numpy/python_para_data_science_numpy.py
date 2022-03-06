# <font color=green> PYTHON PARA DATA SCIENCE - NUMPY
---

# <font color=green> 1. INTRODUÇÃO AO PYTHON
---

# 1.1 Introdução

> Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares. 
>
> Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assunto é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.

# 1.2 Instalação e ambiente de desenvolvimento

### Instalação Local

### https://www.python.org/downloads/
### ou
### https://www.anaconda.com/distribution/

### Google Colaboratory

### https://colab.research.google.com

### Verificando versão

!python -V

"""# 1.3 Trabalhando com arrays Numpy"""

import numpy as np

km = np.loadtxt('carros-km.txt')

km

anos = np.loadtxt('carros-anos.txt', dtype = int)

anos













"""### Obtendo a quilometragem média por ano"""

km_media = km / (2019 - anos)

km_media

type(km_media)

"""# <font color=green> 2. CARACTERÍSTICAS BÁSICAS DA LINGUAGEM
---

# 2.1 Operações matemáticas

### Operadores aritméticos: $+$, $-$, $*$, $/$, $**$, $\%$, $//$

### Adição ($+$)
"""

2 + 2

"""### Subtração ($-$)"""

2 - 2

"""### Multiplicação ($*$)"""

2*3

"""### Divisão ($/$) e ($//$)
A operação divisão sempre retorna um número de ponto flutuante
"""

10/3

10 // 3

"""### Exponenciação ($**$)"""

2 ** 3

"""### Resto da divisão ($\%$)"""

10 % 3

10 % 2

"""### Expressões matemáticas"""

5 * 2 + 3 * 2

(5 * 2) + (3 * 2)

5 * (2 + 3) * 2

"""### A variável _

No modo interativo, o último resultado impresso é atribuído à variável _
"""

5 * 2

_ + 2 * 3

_ / 2

"""# 2.2 Variáveis

### Nomes de variáveis

- Nomes de variáveis pode começar com letras (a - z, A - Z) ou o caractere *underscore* (_):

    > Altura
    >
    > _peso
    
- O restante do nome pode conter letras, números e o caractere "_":

    > nome_da_variavel
    >
    > _valor
    >
    > dia_28_11_
    

- O nomes são *case sensitive*:

    > Nome_Da_Variável $\ne$ nome_da_variavel $\ne$ NOME_DA_VARIAVEL
    
### <font color=red>Observações:
- Existem algumas palavras reservadas da linguagem que não podem ser utilizadas como nomes de variável:

| |Lista de palavras <br>reservadas em Python| |
|:-------------:|:------------:|:-------------:|
| and           | as           | not           | 
| assert        | finally      | or            | 
| break         | for          | pass          | 
| class         | from         | nonlocal      | 
| continue      | global       | raise         | 
| def           | if           | return        | 
| del           | import       | try           | 
| elif          | in           | while         | 
| else          | is           | with          | 
| except        | lambda       | yield         | 
| False         | True         | None          |

### Declaração de variáveis

### Operadores de atribuição: $=$, $+=$, $-=$, $*=$, $/=$, $**=$, $\%=$, $//=$
"""

ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0

ano_atual

ano_fabricacao

km_total

"""# $$km_{média} = \frac {km_{total}}{(Ano_{atual} - Ano_{fabricação})}$$

### Operações com variáveis
"""

km_media = km_total / (ano_atual - ano_fabricacao)
km_media

ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
km_media

ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)

km_total = km_total + km_media
km_total

ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410.0
km_media = km_total / (ano_atual - ano_fabricacao)

km_total += km_media
km_total

"""### Conclusão:
```
"valor = valor + 1" é equivalente a "valor += 1"
```

### Declaração múltipla
"""

ano_atual, ano_fabricacao, km_total = 2019,2003,44410.0

ano_atual

ano_fabricacao

km_total

ano_atual, ano_fabricacao, km_total = 2019,2003,44410.0
km_media = km_total / (ano_atual - ano_fabricacao)
km_media

"""# 2.3 Tipos de dados

Os tipos de dados especificam como números e caracteres serão armazenados e manipulados dentro de um programa. Os tipos de dados básicos do Python são:

1. **Números**
    1. ***int*** - Inteiros
    - ***float*** - Ponto flutuante
- **Booleanos** - Assume os valores True ou False. Essencial quando começarmos a trabalhar com declarações condicionais
- ***Strings*** - Sequência de um ou mais caracteres que pode incluir letras, números e outros tipos de caracteres. Representa um texto.
- **None** - Representa a ausência de valor

### Números
"""

ano_atual = 2019

type(ano_atual)

km_total = 44410.0

type(km_total)

"""### Booleanos"""

zero_km = True

type(zero_km)

zero_km = False

type(zero_km)

"""### Strings"""

nome = 'Jetta Variant'
nome

nome = "Jetta Variant"
nome

nome = 'Jetta "Variant"'
nome

nome = "Jetta 'Variant'"
nome

carro = '''
  Nome
  Idade
  Nota
'''

carro

"""### None"""

quilometragem = None
quilometragem

type(quilometragem)

"""# 2.4 Conversão de tipos"""

a = 10
b = 20
c = 'Python é '
d = 'legal'

type(a)

type(b)

type(c)

type(d)

a + b

c + d

# c + a

"""### Conversões de tipo

Funções int(), float(), str()
"""

str(a)

type(str(a))

c + str(a)

float(a)

var = 3.141592

int(var)

var = 3.99

int(var)

"""# 2.5 Indentação, comentários e formatação de *strings*

### Indentação

Na linguagem Python os programas são estruturados por meio de indentação. Em qualquer linguagem de programação a prática da indentação é bastante útil, facilitando a leitura e também a manutenção do código. Em Python a indentação não é somente uma questão de organização e estilo, mas sim um requisito da linguagem.
"""

ano_atual = 2019
ano_fabricacao = 2019

if (ano_atual == ano_fabricacao):
    print('Verdadeiro')
else:
    print('Falso')

"""### Comentários

Comentários são extremamente importantes em um programa. Consiste em um texto que descreve o que o programa ou uma parte específica do programa está fazendo. Os comentários são ignorados pelo interpretador Python. 

Podemos ter comentários de uma única linha ou de múltiplas linhas.
"""

# Isto é um comentário
ano_atual = 2019
ano_atual

# Isto
# é um 
# comentário
ano_atual = 2019
ano_atual

'''Isto é um
comentário'''
ano_atual = 2019
ano_atual

# Definindo variáveis
ano_atual = 2019
ano_fabricacao = 2019

'''
Estrutura condicional que vamos 
aprender na próxima aula
'''
if (ano_atual == ano_fabricacao):   # Testando se condição é verdadeira
    print('Verdadeiro')
else:                               # Testando se condição é falsa
    print('Falso')

"""### Formatação de *strings*

## *str % valor*
https://docs.python.org/3.6/library/stdtypes.html#old-string-formatting
"""











"""## *str.format()*

https://docs.python.org/3.6/library/stdtypes.html#str.format
"""

print('Olá, {}!'.format('Raphael'))

print('Olá, {}! Este é seu acesso de número {}'.format('Raphael', 32))

print('Olá, {nome}! Este é seu acesso de número {acessos}'.format(nome = 'Raphael', acessos = 32))

"""## *f-Strings*

https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings
"""

nome = 'Raphael'
acessos = 32

print(f'Olá, {nome}! Este é seu acesso de número {acessos}')

"""# <font color=green> 3. TRABALHANDO COM LISTAS
---

# 3.1 Criando listas

Listas são sequências **mutáveis** que são utilizadas para armazenar coleções de itens, geralmente homogêneos. Podem ser construídas de várias formas:
```
- Utilizando um par de colchetes: [ ], [ 1 ]
- Utilizando um par de colchetes com itens separados por vírgulas: [ 1, 2, 3 ]
```
"""

Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

"""### Lista com tipos de dados variados"""

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]

Carro_1

Carro_2

Carros = [Carro_1,Carro_2]
Carros

"""# 3.2 Operações com listas

https://docs.python.org/3.6/library/stdtypes.html#common-sequence-operations

## *x in A*

Retorna **True** se um elemento da lista *A* for igual a *x*.
"""

Acessorios

'Rodas de liga' in Acessorios

'4 x 4' in Acessorios

'Rodas de liga' not in Acessorios

'4 x 4' not in Acessorios

"""## *A + B*

Concatena as listas *A* e *B*.
"""

A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

A

B

A + B

"""## *len(A)*

Tamanho da lista A.
"""

len(Acessorios)

"""# 3.3 Seleções em listas

## *A[ i ]*

Retorna o i-ésimo item da lista *A*.

<font color=red>**Observação:**</font> Listas têm indexação com origem no zero.
"""

Acessorios

Acessorios[0]

Acessorios[1]

Acessorios[-1]

Carros

Carros[0]

Carros[0][0]

Carros[0][-2]

Carros[0][-2][1]

"""## *A[ i : j ]*

Recorta a lista *A* do índice i até o j. Neste fatiamento o elemento com índice i é **incluído** e o elemento com índice j **não é incluído** no resultado.
"""

Acessorios

Acessorios[2:5]

Acessorios[2:]

Acessorios[:5]

"""# 3.4 Métodos de listas

https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types

## *A.sort()*

Ordena a lista *A*.
"""

Acessorios

Acessorios.sort()
Acessorios

"""## *A.append(x)*

Adiciona o elemnto *x* no final da lista *A*.
"""

Acessorios.append('4 X 4')
Acessorios

"""## *A.pop(i)*

Remove e retorna o elemento de índice i da lista *A*.

<font color=red>**Observação:**</font> Por *default* o método *pop()* remove e retorna o último elemento de uma lista.
"""

Acessorios.pop()

Acessorios

Acessorios.pop(3)

Acessorios

"""## *A.copy()*

Cria uma cópia da lista *A*.

<font color=red>**Observação:**</font> O mesmo resultado pode ser obtido com o seguinte código: 
```
A[:]
```
"""

Acessorios_2 = Acessorios
Acessorios_2

Acessorios_2.append('4 X 4')
Acessorios_2

Acessorios

Acessorios.pop()
Acessorios

Acessorios_2

Acessorios_2 = Acessorios.copy()
Acessorios_2

Acessorios_2.append('4 X 4')
Acessorios_2

Acessorios

Acessorios_2 = Acessorios[:]
Acessorios_2



"""# <font color=green> 4. ESTRUTURAS DE REPETIÇÃO E CONDICIONAIS
---

# 4.1 Instrução *for*

#### Formato padrão

```
for <variável> in <coleção>:
    <instruções>
```

### Loops com listas
"""

Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

for item in Acessorios:
  print(item)

"""###  List comprehensions

https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions

*range()* -> https://docs.python.org/3.6/library/functions.html#func-range
"""

range(10)

list(range(10))

for i in range(10):
  print(i ** 2)

quadrado = []
for i in range(10):
  quadrado.append(i ** 2)

quadrado

[i ** 2 for i in range(10)]





"""# 4.2 Loops aninhados"""

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados

for lista in dados:
  print(lista)

for lista in dados:
  for item in lista:
    print(item)

Acessorios = []
for lista in dados:
  for item in lista:
    Acessorios.append(item)

Acessorios

"""## *set()*

https://docs.python.org/3.6/library/stdtypes.html#types-set

https://docs.python.org/3.6/library/functions.html#func-set
"""

list(set(Acessorios))

"""### List comprehensions"""

[item for lista in dados for item in lista]

list(set([item for lista in dados for item in lista]))

"""# 4.3 Instrução *if*

#### Formato padrão

```
if <condição>:
     <instruções caso a condição seja verdadeira>
```

### Operadores de comparação: $==$, $!=$, $>$, $<$, $>=$, $<=$
### e
### Operadores lógicos: $and$, $or$, $not$
"""

# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados

zero_km_Y = []
for lista in dados:
  if(lista[2] == True):
    zero_km_Y.append(lista)

zero_km_Y

zero_km_N = []
for lista in dados:
  if(lista[2] == False):
    zero_km_N.append(lista)

zero_km_N

"""### List comprehensions"""

[lista for lista in dados if(lista[2] == True)]

[lista for lista in dados if(lista[2] == False)]

"""# 4.4 Instruções *if-else* e *if-elif-else*

#### Formato padrão

```
if <condição>:
    <instruções caso a condição seja verdadeira>
else:
    <instruções caso a condição não seja verdadeira>
```
"""

zero_km_Y, zero_km_N = [],[]

for lista in dados:
  if(lista[2] == True):
    zero_km_Y.append(lista)
  else:
    zero_km_N.append(lista)

zero_km_Y

zero_km_N

"""#### Formato padrão

```
if <condição 1>:
    <instruções caso a condição 1 seja verdadeira>
elif <condição 2>:
    <instruções caso a condição 2 seja verdadeira>
elif <condição 3>:
    <instruções caso a condição 3 seja verdadeira>
                        .
                        .
                        .
else:
    <instruções caso as condições anteriores não sejam verdadeiras>
```
"""

dados

print('AND')
print(f'(True and True) o resultado é: {True and True}')
print(f'(True and False) o resultado é: {True and False}')
print(f'(False and True) o resultado é: {False and True}')
print(f'(False and False) o resultado é: {False and False}')

print('OR')
print(f'(True or True) o resultado é: {True or True}')
print(f'(True or False) o resultado é: {True or False}')
print(f'(False or True) o resultado é: {False or True}')
print(f'(False or False) o resultado é: {False or False}')

A, B, C = [], [], []

for lista in dados:
  if(lista[1] <= 2000):
    A.append(lista)
  elif(lista[1] > 2000 and lista[1] <= 2010):
    B.append(lista)
  else:
    C.append(lista)

A

B

C

A, B, C = [], [], []

for lista in dados:
  if(lista[1] <= 2000):
    A.append(lista)
  elif(2000 < lista[1] <= 2010):
    B.append(lista)
  else:
    C.append(lista)

"""# <font color=green> 5. NUMPY BÁSICO
---

Numpy é a abreviação de Numerical Python e é um dos pacotes mais importantes para processamento numérico em Python. Numpy oferece a base para a maioria dos pacotes de aplicações científicas que utilizem dados numéricos em Python (estruturas de dados e algoritmos). Pode-se destacar os seguintes recursos que o pacote Numpy contém:

- Um poderoso objeto array multidimensional;
- Funções matemáticas sofisticadas para operações com arrays sem a necessidade de utilização de laços *for*;
- Recursos de algebra linear e geração de números aleatórios

Além de seus óbvios usos científicos, o pacote NumPy também é muito utilizado em análise de dados como um eficiente contêiner multidimensional de dados genéricos para transporte entre diversos algoritmos e bibliotecas em Python.

**Versão:** 1.16.5

**Instalação:** https://scipy.org/install.html

**Documentação:** https://numpy.org/doc/1.16/

### Pacotes

Existem diversos pacotes Python disponíveis para download na internet. Cada pacote tem como objetivo a solução de determinado tipo de problema e para isso são desenvolvidos novos tipos, funções e métodos.

Alguns pacotes são bastante utilizados em um contexto de ciência de dados como por exemplo:

- Numpy
- Pandas
- Scikit-learn
- Matplotlib

Alguns pacotes não são distribuídos com a instalação default do Python. Neste caso devemos instalar os pacotes que necessitamos em nosso sistema para podermos utilizar suas funcionalidades.

### Importando todo o pacote
"""

import numpy

"""https://numpy.org/doc/1.16/reference/generated/numpy.arange.html"""

numpy.arange(10)

"""### Importando todo o pacote e atribuindo um novo nome """

import numpy as np

np.arange(10)

"""### Importando parte do pacote"""

from numpy import array

arange(10)

"""# 5.1 Criando arrays Numpy"""

import numpy as np

"""### A partir de listas

https://numpy.org/doc/1.16/user/basics.creation.html
"""

km = np.array([1000,2300,4987,1500])

km

type(km)

"""https://numpy.org/doc/1.16/user/basics.types.html"""

km.dtype

"""### A partir de dados externos

https://numpy.org/doc/1.16/reference/generated/numpy.loadtxt.html
"""

km = np.loadtxt(fname = 'carros-km.txt', dtype = int)

km

km.dtype

"""### Arrays com duas dimensões"""

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados

Acessorios = np.array(dados)

Acessorios

km.shape

Acessorios.shape

"""### Comparando desempenho com listas"""

np_array = np.arange(1000000)

py_list = list(range(1000000))

# Commented out IPython magic to ensure Python compatibility.
# %time for _ in range(100): np_array *= 2

# Commented out IPython magic to ensure Python compatibility.
# %time for _ in range(100): py_list = [x * 2 for x in py_list]

"""# 5.2 Operações aritméticas com arrays Numpy

### Operações entre arrays e constantes
"""

km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]

# idade = 2019 - anos

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2019 - anos

idade

"""### Operações entre arrays"""

km_media = km / idade

km_media

44410 / (2019-2003)

5712 / (2019-1991)

"""### Operações com arrays de duas dimensões"""

dados = np.array([km, anos])

dados

dados.shape

"""![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)"""

dados[0]

dados[1]

km_media = dados[0] / (2019 - dados[1])

km_media

"""# 5.3 Seleções com arrays Numpy

![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)
"""

dados

"""![1410-img02.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img02.png)

### Indexação 

<font color=red>**Observação:**</font> A indexação tem origem no zero.
"""

contador = np.arange(10)
contador

contador[0]

item = 6
index = item -1
contador[index]

contador[-1]

dados[0]



"""## <font color=green>**Dica:**</font>
### *ndarray[ linha ][ coluna ]* ou *ndarray[ linha, coluna ]*
"""

dados[1][2]

dados[1,2]

"""### Fatiamentos
 
A sintaxe para realizar fatiamento em um array Numpy é $i : j : k$ onde $i$ é o índice inicial, $j$ é o índice de parada, e $k$ é o indicador de passo ($k\neq0$)
 
<font color=red>**Observação:**</font> Nos fatiamentos (*slices*) o item com índice i é **incluído** e o item com índice j **não é incluído** no resultado.

![1410-img01.png](https://caelum-online-public.s3.amazonaws.com/1410-pythondatascience/01/1410-img01.png)
"""

contador = np.arange(10)
contador

contador[1:4]

contador[1:8:2]

contador[::2]

contador[1::2]

dados

dados[:, 1:3]

dados[:, 1:3][0] / (2019 - dados[:, 1:3][1])

dados[0] / (2019 - dados[1])

"""### Indexação com array booleano

<font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou um array booleano.
"""

contador = np.arange(10)
contador

contador > 5

contador[contador > 5]

contador[[False, False, False, False, False, False,  True,  True,  True,
        True]]

dados

dados[1] > 2000

dados[:, dados[1] > 2000]

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
)

dados[0::2, :2]

dados[:2, :2]

dados[:2, 0::2]

"""# 5.4 Atributos e métodos de arrays Numpy"""

dados = np.array([[44410.,  5712., 37123.,     0., 25757.],
                  [2003,  1991,  1990,  2019,  2006]])
dados

"""### Atributos

https://numpy.org/doc/1.16/reference/arrays.ndarray.html#array-attributes
"""

dados.shape

"""## *ndarray.shape*

Retorna uma tupla com as dimensões do array.
"""

dados.shape

"""## *ndarray.ndim*

Retorna o número de dimensões do array.
"""

dados.ndim

"""## *ndarray.size*

Retorna o número de elementos do array.
"""

dados.size

"""## *ndarray.dtype*

Retorna o tipo de dados dos elementos do array.
"""

dados.dtype

"""## *ndarray.T*

Retorna o array transposto, isto é, converte linhas em colunas e vice versa.
"""

dados.T

dados.transpose()

"""### Métodos

https://numpy.org/doc/1.16/reference/arrays.ndarray.html#array-methods

## *ndarray.tolist()*

Retorna o array como uma lista Python.
"""

dados.tolist()

"""## *ndarray.reshape(shape[, order])*

Retorna um array que contém os mesmos dados com uma nova forma.
"""

contador = np.arange(10)
contador

contador.reshape((5,2))

contador.reshape((5,2), order='C')

contador.reshape((5,2), order='F')

km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]

info_carros = km + anos
info_carros

np.array(info_carros).reshape((2,5))

np.array(info_carros).reshape((5,2), order='F')

"""## *ndarray.resize(new_shape[, refcheck])*

Altera a forma e o tamanho do array.
"""

dados_new = dados.copy()
dados_new

dados_new.resize((3,5), refcheck=False)

dados_new

dados_new[2] = dados_new[0] / (2019 - dados_new[1])

dados_new



"""# 5.5 Estatísticas com arrays Numpy

https://numpy.org/doc/1.16/reference/arrays.ndarray.html#calculation

e

https://numpy.org/doc/1.16/reference/routines.statistics.html

e

https://numpy.org/doc/1.16/reference/routines.math.html
"""

anos = np.loadtxt(fname = "carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "carros-km.txt")
valor = np.loadtxt(fname = "carros-valor.txt")

anos.shape

"""https://numpy.org/doc/1.16/reference/generated/numpy.column_stack.html"""

dataset = np.column_stack((anos, km, valor))
dataset

dataset.shape

"""## *np.mean()*

Retorna a média dos elementos do array ao longo do eixo especificado.
"""

np.mean(dataset, axis = 0)

np.mean(dataset, axis = 1)

np.mean(dataset[:,1])

np.mean(dataset[:,2])

"""## *np.std()*

Retorna o desvio padrão dos elementos do array ao longo do eixo especificado.
"""

np.std(dataset[:,2])

"""## *ndarray.sum()*

Retorna a soma dos elementos do array ao longo do eixo especificado.
"""

dataset.sum(axis = 0)

dataset[:,1].sum()

"""## *np.sum()*

Retorna a soma dos elementos do array ao longo do eixo especificado.
"""

np.sum(dataset, axis = 0)

np.sum(dataset[:, 2])

