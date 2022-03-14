# Importando e normalizando o corpus do corretor

# carregando a base de dados (corpus do NLP) e atribuindo a uma variável
with open("artigos.txt", "r") as f:
  artigos = f.read()

# lendo os primeiros 500 caracteres para validar a leitura dos dados
print(artigos[:500])

# com o len podemos verificar o número de letras existentes no corpus
len(artigos)

len("Olá")

texto_exemplo = "Olá, tudo bem?"
palavras_separadas = texto_exemplo.split()
print(palavras_separadas)

print(len(palavras_separadas))

# ao utilizarmos o comando .split() criamos uma lista com uma separação de sentenças de textos, porém como na separação ele engloba símbolso como ,?! agregado a plavravas damos o nome dessa separação de token
texto_exemplo = "Olá, tudo bem?"
tokens = texto_exemplo.split()
print(tokens)
print(len(tokens))

# a biblioteca nltk possuem funções que fazem a separação mais precisa de palavras em um texto
# com o comando nltk.tokenize.word_tokenize separamos as palavras em uma nova variável 
import nltk 
nltk.download('punkt')
palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)

print(palavras_separadas)

len(palavras_separadas)

# com o comando .isalpha podemos verificar um str e verificar se ela possue apenas letras ou não
'palavra1'.isalpha()

# criando uma função podemos rodar um for com o comando .isalpha em nossa lista de tokens criados pelo comando nltk para separar em uma nova lista apenas palavras
def separa_palavras(lista_tokens):
  lista_palavras = []
  for token in lista_tokens:
    if token.isalpha():
      lista_palavras.append(token)
  return lista_palavras

separa_palavras(palavras_separadas)

# unindo conceitos, encontramos no corpus a quantidade de palavras disponíveis
lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
print(f"O número de palavras em nosso corpus é {len(lista_palavras)}")

print(lista_palavras[:5])

# para contar os tipos de palavras primeiro precizamos normalizar o texto removendo qualquer tipo de maíscula nos caracteres
# com a função normalização tornamos todos os caracteres do curpus em letras minúsculas
def normalizacao(lista_palavras):
  lista_normalizada = []
  for palavra in lista_palavras:
    lista_normalizada.append(palavra.lower())
  return lista_normalizada

lista_normalizada = normalizacao(lista_palavras)
print(lista_normalizada[:5])

# com o comando set() agrupamos em uma lista os item únicos de uma lista
set([1,2,3,3,3,5,6,6,6,7])

# aplicando o len junto ao set podemos obter a quantidade de palavras únicas dentro o corpus
len(set(lista_normalizada))

"""# 1ª Solução do corretor - Inserindo caracter faltante na palavra errada"""

lista = 'lgica'
(lista[:1],lista[1:])

palavra_exemplo = 'lgica'

# o primeiro passo para criação do corretor é através do impute de uma palavra errada, gerar as multiplas palavras que podem ser geradas a partir desta adicionando todas as letras do alfabeto em todas as posições possíveis
# para gerar a lista de novas palavras criamos uma função para inserir letras e uma outra com um gerador de novas palavras

def insere_letras(fatias):
  novas_palavras = []
  letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras

def gerador_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)

def corretor (palavra):
  palavras_geradas = gerador_palavras(palavra)
  palavra_correta = max(palavras_geradas, key=probabilidade)
  return palavra_correta

# com o comando nltk.FreqDist temos uma lista de tuplas com a palavra e a quantidade de vezes que a mesma é repedita no corpus
frequencia = nltk.FreqDist(lista_normalizada)
total_palavras = len(lista_normalizada)
frequencia.most_common(10)

def probabilidade(palavra_gerada):
  return frequencia[palavra_gerada]/total_palavras
probabilidade("lógica")

palavra_exemplo = 'lgica'
corretor(palavra_exemplo)

def cria_dados_teste(nome_arquivo):
  lista_palavras_teste = []
  f = open(nome_arquivo, "r")
  for linha in f:
    correta, errada = linha.split()
    lista_palavras_teste.append((correta, errada))
  f.close()
  return lista_palavras_teste

lista_teste = cria_dados_teste("palavras.txt")
lista_teste

# função avaliador para verificar o percentual de correção do corretor com apenas uma solução aplicada
def avaliador (testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras")

avaliador(lista_teste)

"""# 2ª Solução do corretor - Deletando caracter errado na palavra errada"""

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

# com a atualização da função gerador de palavras adicionando a função deletando caracteres otimizamos o corretor
def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    return palavras_geradas
palavra_exemplo = "lóigica"
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)

avaliador(lista_teste)

"""# 3ª Solução do corretor - Alterando caracter errado na palavra *errada*"""

# função para geração de novas palavras com as trocas de letras
def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

# agrupando as soluções criadas no corretor
def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    return palavras_geradas

palavra_exemplo = "lígica"
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)

"""# 4ª Solução do corretor - Invertendo caracteres na palavra *errada*"""

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras

def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

# implementando com a função inverte letra
def inverte_letra(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    palavras_geradas += inverte_letra(fatias)
    return palavras_geradas

palavra_exemplo = "lgóica"
palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)

avaliador(lista_teste)

"""# Calculando a taxa de palavras desconhecidas pelo corretor"""

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            desconhecida += (correta not in vocabulario)
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas é {taxa_desconhecida}%")


vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

"""# 5ª Solução do corretor - Implementando a verificação em loop para corrigir dois erros na palavra *errada*"""

# simulando a palavra lógica digitada com dois erros, implementando um for que cria novas palavras a partir das primeiras palavras criadas, conseguimos montar uma lista com a palavra correta
palavra = "lóiigica"

def gerador_turbinado(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras

palavras_g = gerador_turbinado(gerador_palavras(palavra))
"lógica" in palavras_g

# no entanto temos um volume significativo de palavras o que pode pesar o corretor a encontrar a palavra correta de forma otimizada
len(palavras_g)

# otimizando a função corretor diminuindo o número de palavras possíveis para verificação
def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavras_turbinado = gerador_turbinado(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_turbinado)
    candidatos = [palavra]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)
    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta

novo_corretor(palavra)

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = novo_corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            desconhecida += (correta not in vocabulario)
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

# avaliando a implementação do novo corretor tivemos uma redução na taxa de palavras corrigidas
def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = novo_corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

"""# Avaliando"""

# avaliando as palavras geradas identificamos que na maioria das vezes o erro de digitação está em sua maioria a uma distância de ser corrigido, por este motivo ao gerarmos duas correções geramos palavras diferentes das corretas
def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = novo_corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            print(errada + "-" + corretor(errada) + "-" + palavra_corrigida)
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

# concluímos que a primeira versão do corretor é mais acertiva ao determinar a palavra errada digitada
def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")

vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)

# comparando os resultados dos corretores
palavra = "lgica"
print('Corretor turbinado -> '+ novo_corretor(palavra))
print('Corretor de verificação única -> '+ corretor(palavra))