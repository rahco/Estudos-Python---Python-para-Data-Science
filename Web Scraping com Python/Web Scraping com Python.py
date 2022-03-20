#!/usr/bin/env python
# coding: utf-8

# # <font color=green>1. MEU PRIMEIRO SCRAPING

# # 1.1. Introdução

# ## *Web Scraping* é o termo utilizado para definir a prática de coletar automaticamente informações na Internet. Isto é feito, geralmente, por meio de programas que simulam a navegação humana na Web.

# # 1.2. Ambiente e bibliotecas
# ### Utilizaremos em nosso treinamento o navegador Google Chrome

import bs4
import urllib.request as urllib_request
import pandas

print("BeautifulSoup ->", bs4.__version__)
print("urllib ->", urllib_request.__version__)
print("pandas ->", pandas.__version__)

# # 1.3. Meu primeiro scraping

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
soup

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.find('h1', id="hello-world").get_text())
print(soup.find('p').get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

soup.find('h1', {'class': 'sub-header'}).get_text()

# ---
# # <font color=green>2. OBTENDO E TRATANDO O CONTEÚDO DE UM HTML

# # 2.1. Entendendo a web

# <img src="./web/web.png" width="700">

# # 2.2. Obtendo o conteúdo HTML de um site

# # urllib.request
# ## https://docs.python.org/3/library/urllib.html

# importando a função urlopen da biblioteca urllib.request podemoa atribuir o conteúdo html de uma página web a uma variável
# atribuindo a outra varável com o comando .read() podemos ler o código html no console

from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()
html

# ## https://docs.python.org/3/library/urllib.request.html#urllib.request.Request

# para alguns sites precisamos da função Request para inserir o User-Agent de acesso para conseguir ler o código
# inicialmente atribuimos a uma variável a funçaõ Request com os parâmetros de url e headers
# atribuimos o variável/Request ao urlopen() e assim conseguimos acesso ao código html da página
# o User-Agent pode ser acessano no chrome com a página aberta e precionando a tecla f12: Network + F5(para atualizar a página) > Acessar qualquer item > Headers > Request Headers

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

req = Request(url, headers = headers)
response = urlopen(req)
print(response.read())

# com a bilioteca .error podemos utilizar o HTTPError para printarmos o erro de acesso
# abaixo removemos o parâmetro Headers apenas para verificar o erro 403 Forbidden
# o URLError print uma mensagem [Errno 11001] getaddrinfo failed informando que o url está digitado errado

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

try:
    req = Request(url)
    response = urlopen(req)
    print(response.read())

except HTTPError as e:
    print(e.status, e.reason)
    
except URLError as e:
  print(e.reason)

# com a bilioteca .error podemos utilizar o HTTPError para printarmos o erro de acesso
# abaixo removemos o parâmetro Headers apenas para verificar o erro 403 Forbidden
# o URLError print uma mensagem [Errno 11001] getaddrinfo failed informando que o url está digitado errado

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alurua.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    print(response.read())

except HTTPError as e:
    print(e.status, e.reason)
    
except URLError as e:
  print(e.reason)

# # 2.3. Tratamento de string

from urllib.request import urlopen

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()
html

# ### Convertando o tipo bytes para string

type(html)

# com o comando .decode() convertemos o tipo html para str, corrindo erros de textos como ç e acentuações

html = html.decode('utf-8')

type(html)

html

# ### Eliminando os caracteres de tabulação, quebra de linha etc.

# com o comando .split() criamos uma lista com as 'palavras' contidas no código html

html.split()

# com o comando .join inserimos um espaço entre as 'palavras' limpando mais o código

" ".join(html.split())

# ### Eliminando os espaços em branco entre as TAGS

# com o .replace otimizamos a limpeza dos dados consolidando mais as informações

" ".join(html.split()).replace('> <', '><')

# ### Função de tratamento de strings

# para facilitar o uso atribuimos todos os comandos de edição em uma função chamada trata_html com o url a ser usado como input

def trata_html(input):
    return " ".join(input.split()).replace('> <', '><')

html

html = trata_html(html)
html

# exemplo de aplicação das tratativas por fase

string = 'O\ns@po\nn#o\tl@v@\to\npé'

# com split dividimos as palavras cortadas nos \n e \t

" ".join(string.split())

# com o replace substituimos caracteres errados

" ".join(string.split()).replace('@', 'a').replace('#', 'ã')

# ---
# # <font color=green>3. INTRODUÇÃO AO BEAUTIFULSOUP

# # 3.1. HTML da nossa página

# **HTML** (*HyperText Markup Language*) é uma linguagem de marcação composta por **tags** que deteminam o papel que cada parte do documento vai assumir. As **tags** são formadas pelo seu nome e atributos. Os atributos servem para configurar e também modificar as características padrões de uma **tag**.
# 
# ## Estrutura básica
# 
# ```html
# <html>
#     <head>
#         <meta charset="utf-8" />
#         <title>Alura Motors</title>
#     </head>
#     <body>
#         <div id="container">
#             <h1>Alura</h1>
#             <h2 class="formato">Cursos de Tecnologia</h2>
#             <p>Você vai estudar, praticar, discutir e aprender.</p>
#             <a href="https://www.alura.com.br/">Clique aqui</a>
#         </div>
#     </body>
# </html>
# ```
# 
# ```<html>``` - determina o início do documento.
# 
# ```<head>``` - cabeçalho. Contém informações e configurações do documento.
# 
# ```<body>``` - é o corpo do documento, onde todo o conteúdo é colocado. Esta é a parte visível em um navegador.
# 
# ## Tags mais comuns
# 
# ```<div>``` - define uma divisão da página. Pode ser formatada de diversas maneiras.
# 
# ```<h1>, <h2>, <h3>, <h4>, <h5>, <h6>``` - marcadores de títulos.
# 
# ```<p>``` - marcador de parágrafo.
# 
# ```<a>``` - hiperlink.
# 
# ```<img>``` - exibição de imagens.
# 
# ```<table>``` - definição de tabelas.
# 
# ```<ul>, <li>``` - definição de listas.
# 

# # 3.2. Criando um objeto BeautifulSoup

# ## https://www.crummy.com/software/BeautifulSoup/
# 
# ### Sobre parser ver: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parser-installation

# com a biblioteca bs4 importamos o BeautifulSoup que é uma função que transforma o código html em um objeto de fácil leitura
# o BeautifulSoup oferece um conjunto de métodos simples, para possibilitar a navegação, pesquisa e alteração de documentos 
# nos formatos HTML e XML.

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

soup

# com a alteração temos um novo objeto em type

type(soup)

# ao executarmos o print do objeto BeautifulSoup com o comando .prettify() temos uma visualização mais organizada do código

print(soup.prettify())

# # 3.3. Acessando tags

soup

# acessando os níveis das informações com . podemos navegar entre as tags para coletar dados

soup.html.head.title

# outra forma de acessar é apenas indicando uma tag, porém neste caso ele irá percorrer a página e trazer a primeira que encontrar

soup.title

soup.div

soup.div.div.div.div.h5

# # 3.4. Acessando o conteúdo das tags

soup.html.head.title

soup.title

# com o comando .get_text() conseguimos acessar o conteúdo da tag

soup.title.get_text()

soup.h5

soup.h5.get_text()

# utilizando o parâmetro separator, conseguimos definir um separador para extrair textos de tags de forma geral

soup2 = BeautifulSoup('<h1>Título 1</h1><h2>Título 1.1</h2><p>Conteúdo</p>')
soup2.get_text(' # ')

# com o parâmetro strip definido como True podemos remover os espaços em brancos do início e fim de cada bloco

from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Texto de conteúdo A</p>
                <div id="container-a-1">
                    <h1>Título A.1</h1>
                    <h2 class="ref-a">Sub título A.1</h2>
                    <p>Texto de conteúdo A.1</p>
                </div>
            </div>
        </body>
    </html>
"""
soup3 = BeautifulSoup(html, 'html.parser')
soup3

soup3.get_text(separator=' || ', strip=True)

# # 3.5. Acessando os atributos de uma tag

# ao consultarmos apenas .img consultamos a primeira imagem encontrada no código html

soup.img

# com o comando .attrs, criamos um dicionário com o conteúdo da tag. Tendo dois valores eles são agrupados em uma lista junto a sua chave

soup.img.attrs

# com o comando .attrs.keys() conseguimos uma lista com apenas as chaves do dicionário

soup.img.attrs.keys()

# com o comando .attrs.values() conseguimos uma lista com apenas os valores do dicionário

soup.img.attrs.values()

# com [] acessamos ao conteúdo específico de uma chave

soup.img['class']

# com o comando .get() pegamos o endereço da imagem

soup.img.get('src')

# ---
# # <font color=green>4. PESQUISANDO COM O BEAUTIFULSOUP

# # 4.1. Os métodos *find()* e *findAll()*

# - ### *find(tag, attributes, recursive, text, **kwargs)*
# 
# - ### *findAll(tag, attributes, recursive, text, limit, **kwargs)*
# 
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
# 
# > **Observação:**
# > - *findAll()* também pode ser utilizado como *find_all()*

# ### Método *find()*

# com o método .find() conseguimos acessar o conteúdo de uma tag
# similar a consulta direta ele trás o primeiro elemento encontrado no código com a tag

soup.find('img')

soup.img

# ### Método *findAll()*

# com o método .findAll conseguimos uma lista com o conteúdo de todas as tags de igual nome

soup.findAll('img')

# ### Comando equivalente ao método *find()*

# como parâmetro limit podemos especificar um limite para a lista. Entre [] é possível definir o item desejado da lista

soup.findAll('img', limit =1)[0]

# ### Atalho para o método *findAll()*

# um atalho para utilizar o método .findAll é apenas colocando a tag desejada entre ()

soup('img')

# ### Passando listas de TAGs

# com o .findAll podemos criar listas com diferentes tags

soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# ### Utilizando o argumento *attributes*

# o comando pode ser utilizado para filtrar uma lista direta de atributos e através de suas características é possível refinar a consulta

soup.findAll('p')

# passando em dicionário podemos filtrar apenas uma classe de dados

soup.findAll('p', {"class": "txt-value"})

# ### Buscando por conteúdo de uma TAG

# o .findAll pode ser utilizado junto ao atributo text para filtrar dados a partir de uma str

soup.findAll('p', text = "Belo Horizonte - MG")

# ### Utilizando diretamente os atributos

# com o parâmetros alt podemos filtrar uma lista direta de fotos

soup.findAll('img', alt = "Foto")

# fazendo uma iteração podemo extrair textos ou endereços dentro do filtro realizado

for item in soup.findAll('img', alt="Foto"): 
  print(item.get('src'))

# ### Cuidado com o atributo "class"

# de forma similar utilizando o parâmetro class temos um erro pois a palavra class é uma palavras reservada

soup.findAll('p', class="txt-value")

# para solucionar o erro adicionamos um underscore _ após a palavras class

soup.findAll('p', class_="txt-value")


# ### Obtendo todo o conteúdo de texto de uma página

# com o parâmetro text como True podemos montar uma lista com todos os textos disponíveis nas tags

soup.findAll(text = True)

# # 4.2. Outros métodos de pesquisa

# - ### *findParent(tag, attributes, text, **kwargs)*
# 
# - ### *findParents(tag, attributes, text, limit, **kwargs)*
# 
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-parents-and-find-parent
# 
# > **Observação:**
# > - *findParent()* e *findParents()* também podem ser utilizados como *find_parent()* e *find_parents()*, respectivamente.
# ---
# - ### *findNextSibling(tag, attributes, text, **kwargs)*
# 
# - ### *findNextSiblings(tag, attributes, text, limit, **kwargs)*
# 
# - ### *findPreviousSibling(tag, attributes, text, **kwargs)*
# 
# - ### *findPreviousSiblings(tag, attributes, text, limit, **kwargs)*
# 
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-previous-siblings-and-find-previous-sibling
# 
# > **Observação:**
# > - *findNextSibling()*, *findNextSiblings()*, *findPreviousSibling()* e *findPreviousSiblings()* também podem ser utilizados como *find_next_sibling()*, *find_next_siblings()*, *find_previous_sibling()* e *find_previous_siblings()*, respectivamente.
# ---
# - ### *findNext(tag, attributes, text, **kwargs)*
# 
# - ### *findAllNext(tag, attributes, text, limit, **kwargs)*
# 
# - ### *findPrevious(tag, attributes, text, **kwargs)*
# 
# - ### *findAllPrevious(tag, attributes, text, limit, **kwargs)*
# 
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all-next-and-find-next
# #### https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all-previous-and-find-previous
# 
# > **Observação:**
# > - *findNext()*, *findAllNext()*, *findPrevious* e *findAllPrevious* também podem ser utilizados como *find_next()*, *find_all_next()*, *find_previous()* e *find_all_previous()*, respectivamente.

# ## HTML de exemplo para ilustrar a utilização dos métodos de pesquisa do BeautifulSoup

# <img src="https://caelum-online-public.s3.amazonaws.com/1381-scraping/01/BeautifulSoup-method.png" width=80%>

# ---
# ## Resultado

# <html>
#     <body>
#         <div id=“container-a”>
#             <h1>Título A</h1>
#             <h2 class="ref-a">Sub título A</h2>
#             <p>Texto de conteúdo A</p>
#         </div>
#         <div id=“container-b”>
#             <h1>Título B</h1>
#             <h2 class="ref-b">Sub título B</h2>
#             <p>Texto de conteúdo B</p>
#         </div>
#     </body>
# </html>

html_teste = """
    <html>
        <body>
            <div id="container-a">
                <h1>Título A</h1>
                <h2 class="ref-a">Sub título A</h2>
                <p>Texto de conteúdo A</p>
            </div>
            <div id="container-b">
                <h1>Título B</h1>
                <h2 class="ref-b">Sub título B</h2>
                <p>Texto de conteúdo B</p>
            </div>
        </body>
    </html>
"""

# ### Tratamentos para a string HTML

html_teste

html_teste = trata_html(html_teste)
html_teste

soup.find('h2')

# ### Criando o objeto BeautifulSoup

soup = BeautifulSoup(html_teste, 'html.parser')
soup

# ### Parents

soup.find('h2')

# com o método parent conseguimos varrer o código buscando dados que estão acima de uma tag selecionada
# no exemplo abaixo encontramos a tag h2 e com o parent chegamos a sua div

soup.find('h2').find_parent('div')

# com o parents conseguimos acessar as tags que são parents da tag filtrada

soup.find('h2').find_parents()

# com o parent podemos também fazer uma iteração gerando uma lista de tags parents

for item in soup.findAll('h2'):
    print(item.find_parent('div'))

# ## Siblings

# com o Sibling conseguimos acessar as tags anteriores ou posteriores a uma tag selecionada

soup.find('h2').findNextSibling()

soup.find('h2').findPreviousSibling()

soup.find('p').findPreviousSiblings()

# ## Next e Previous

# o Next e Previous funciona de forma similar ao Sibling

soup.find('h2').findNext()

soup.find('h2').findPrevious()

soup.find('h2').findAllNext()

# # <font color=green>5. WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE UM ANÚNCIO

# # 5.1. Identificando e selecionando os dados no HTML

# ### Obtendo o HTML e criando o objeto BeautifulSoup

response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
soup

# ### Criando variávels para armazenar informações

cards = []
card = {}

# ### Obtendo os dados do primeiro CARD

anuncio = soup.find('div', {'class': 'well card'})
anuncio

# # 5.2. Obtendo o VALOR do veículo anunciado

anuncio

anuncio.find('div', {'class': 'value-card'})

anuncio.find('p', {'class': 'txt-value'}).getText()

card['value'] = anuncio.find('p', {'class': 'txt-value'}).getText()

card

# ### <font color=red>Resumo

# Valor
card['value'] = anuncio.find('p', {'class': 'txt-value'}).getText()

# # 5.3. Obtendo as INFORMAÇÕES sobre o veículo anunciado

anuncio.find('div', {'class': 'body-card'})

anuncio.find('div', {'class': 'body-card'}).findAll('p')

# para otimizar o código criamos uma nova variável filtrando as tags p do código já filtrando na variável anuncio

infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')

for info in infos:
    print(info)

# iterando sobre a variável temos uma lista com as tags e valores

for info in infos:
    print(info.get('class'), ' - ', info.get_text())

for info in infos:
    print(info.get('class')[0], ' - ', info.get_text())

# utilizando o .split separamos em uma nova array os valores que precisamos
for info in infos:
    print(info.get('class')[0].split('-'), ' - ', info.get_text())

# com o filtro em -1 chegamos a key e o value
for info in infos:
    print(info.get('class')[0].split('-')[-1], ' - ', info.get_text())

# atribuindo a variável card a key e o value, criamos um dicionário com as informações dos cards
for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()

card

# ### <font color=red>Resumo

# Informações
infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()

# # 5.4. Obtendo os ACESSÓRIOS do veículo anunciado

anuncio.find('div', {'class': 'body-card'})

anuncio.find('div', {'class': 'body-card'}).ul

anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')

items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
items

# com o .pop fazemos um tratamento na lista removendo o último item que não possui utilidade
items.pop()

for item in items:
    print(item.getText())

for item in items:
    print(item.getText().replace('► ', ''))

acessorios = []
for item in items:
    acessorios.append(item.getText().replace('► ', ''))

acessorios

card['items'] = acessorios

card

# ### <font color=red>Resumo

# Acessórios
items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
items.pop()
acessorios = []
for item in items:
    acessorios.append(item.getText().replace('► ', ''))
card['items'] = acessorios

# # 5.5 Criando um DataFrame com os dados coletados do Alura Motors

card

import pandas as pd

dataset = pd.DataFrame(card)

dataset

# para resolver o problema dos valores de items que foram todos jogamos e linhas distintas
# utilizamos o método .from_dict que cria um df a partir de um dicionário
dataset = pd.DataFrame.from_dict(card, orient = 'index')
dataset

# com o .T fazemos a transposição do df de linhas para colunas
dataset = pd.DataFrame.from_dict(card, orient = 'index').T
dataset

# com o método .to_csv salvamos o df em um arquivo csv
dataset.to_csv('./output/data/dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')

# # 5.6. Obtendo a FOTO do anúncio

anuncio.find('div', {'class': 'image-card'})

image = anuncio.find('div', {'class': 'image-card'}).img
image

image.get('src')

# com o comando print podemos clicando no link visualizar se o filtro do url funcionou
print(image.get('src'))

# ### Visualizando a FOTO no notebook (extra)

# método para visualizar a foto no notebook

from IPython.core.display import display, HTML

display(HTML(str(anuncio.find('div', {'class': 'image-card'}).img)))

display(HTML("<img src=" + anuncio.find('div', {'class': 'image-card'}).img.get('src') + ">"))

# ### Rotina para acessar e salvar a FOTO do anúncio

# ## https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve

# comando para pegar o nome da imagem
image.get('src').split('/')[-1]

# utilizanso o urlretrieve podemos salvar uma cópia da foto em uma pasta

from urllib.request import urlretrieve

urlretrieve(image.get('src'), './output/img/' + image.get('src').split('/')[-1])

# ### <font color=red>Resumo

# Imagens

image = anuncio.find('div', {'class': 'image-card'}).img
urlretrieve(image.get('src'), './output/img/' + image.get('src').split('/')[-1])

# # <font color=green>6. WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE TODOS OS ANÚNCIOS DE UMA PÁGINA

# # 6.1. Identificando as informações no HTML

# com filtro em container-cards temos todas as informações de todos os cards agrupada

soup.find('div', {"id": "container-cards"})

# filtrando a informações class_=well card chegamos aos dados de cada anuncio

soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")

# utilizamos o len para confirmar a quantidade de anuncios filtrados

len(soup.find('div', {"id": "container-cards"}).findAll('div', class_="card"))

# atribuindo a variável anuncios o filtro dos anuncios

anuncios = soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")

# iterando e utilizando o comando \n\n pulamos duas linhas entre cada anuncio para validarmos a filtragem dos anuncios

for anuncio in anuncios:
    print(str(anuncio) + "\n\n")

# # 6.2. Criando uma rotina de scraping

# Código completo contemplando todos os processos de raspagens das infos do site

# Importando bibliotecas
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Declarando variável cards
cards = []

# Obtendo o HTML
response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# Obtendo as TAGs de interesse
anuncios = soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")

# Coletando as informações dos CARDS
for anuncio in anuncios:
    card = {}

    # Valor
    card['value'] = anuncio.find('p', {'class': 'txt-value'}).getText()

    # Informações
    infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
    for info in infos:
        card[info.get('class')[0].split('-')[-1]] = info.get_text()

    # Acessórios
    items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
    items.pop()
    acessorios = []
    for item in items:
        acessorios.append(item.get_text().replace('► ', ''))
    card['items'] = acessorios

    # Adicionando resultado a lista cards
    cards.append(card)

    # Imagens
    image = anuncio.find('div', {'class': 'image-card'}).img
    urlretrieve(image.get('src'), './output/img/' + image.get('src').split('/')[-1])

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('./output/data/dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')
dataset

# # <font color=green>7. WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE TODOS OS ANÚNCIOS DO SITE

# # 7.1. Identificando as informações no HTML

# localizando a quantidade de páginas com anúncios disponíveis através do código html

soup.find('span', class_="info-pages")

soup.find('span', class_="info-pages").get_text()

soup.find('span', class_="info-pages").get_text().split()

soup.find('span', class_="info-pages").get_text().split()[-1]

# localizando a quantidade de páginas com anúncios disponíveis através do código html

int(soup.find('span', class_="info-pages").get_text().split()[-1])

# outra forma de se obter o número das páginas pode ser utilizando o métido math.ceil

from bs4 import BeautifulSoup

htmls = """
    <html>
        <body>
            <h1>Busca por veículos</h1>
            <div>
                <p id="info-search">Encontramos 1325 anúncios</p>
                <span class="info-pages">20 anúncios por página</span>
            </div>
        </body>
    </html>
"""
soups = BeautifulSoup(htmls, 'html.parser')

import math

# com o math.ceil arredondamos os números de páginas calculada com o número de anúncios sobre a relação qtde_anuncios/página

math.ceil(int(soups.p.get_text().split()[1]) / int(soups.span.get_text().split()[0]))

# # 7.2. Criando uma rotina de scraping

### -> Código completo de scraping do site todo incluindo a navegação entre as páginas

# Importando bibliotecas
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Declarando variável cards
cards = []

## Obtendo o HTML e o total de páginas
### -> Incluindo a variável pages com a quantidade de páginas do site
response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
pages = int(soup.find('span', class_="info-pages").get_text().split()[-1])

## Iterando por todas as páginas do site
### -> Para interar em todas as páginas primeiro identificamos que ao mudar de página o url é alterado adicionando ao final
### -> o texto ?page=2, onde o número representa a página em que se está navegando. Partindo dessa observação adicionamos o
### -> texto ?page= ao final do url iterando em um for com a quantidade de páginas existentes no site conforme variável page
### -> anteriormente criada. O + 1 foi adicionado para corrigir o range que não lia todas as páginas
for i in range(pages):
    ## Obtendo o HTML
    response = urlopen('https://alura-site-scraping.herokuapp.com/index.php?page=' + str(i  + 1))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # Obtendo as TAGs de interesse
    anuncios = soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")

    # Coletando as informações dos CARDS
    for anuncio in anuncios:
        card = {}

        # Valor
        card['value'] = anuncio.find('p', {'class': 'txt-value'}).getText()

        # Informações
        infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
        for info in infos:
                card[info.get('class')[0].split('-')[-1]] = info.get_text()

        # Acessórios
        items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
        items.pop()
        acessorios = []
        for item in items:
            acessorios.append(item.get_text().replace('► ', ''))
        card['items'] = acessorios

        # Adicionando resultado a lista cards
        cards.append(card)

        # Imagens
        image = anuncio.find('div', {'class': 'image-card'}).img
        urlretrieve(image.get('src'), './output/img/' + image.get('src').split('/')[-1])     

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('./output/data/dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')
dataset

