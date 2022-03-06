# Importando base de dados

import pandas as pd

pd.read_csv('tips.csv')

dados = pd.read_csv('tips.csv')

dados.head()

"""# Tradução"""

# comando .columns para visualização dos nomes das colunas do df
dados.columns

renomear = {
    'total_bill' : 'valor_da_conta', 
    'tip' : 'gorjeta', 
    'dessert' : 'sobremesa', 
    'day' : 'dia_da_semana', 
    'time' : 'hora_do_dia', 
    'size' : 'total_de_pessoas'
}

type(dados)

gorjetas = dados.rename(columns = renomear)

gorjetas.head()

# com o comando .unique acessamos todos os tipos de respostas únicos contidos em uma series de um df
gorjetas.sobremesa.unique()

sim_nao = {
    'No' : 'Não', 
    'Yes' : 'Sim'
}

# o comando .map pode ser utilizado para trocar elementos de uma series dentro de um df através de um dicionário pré definido.
gorjetas.sobremesa.map(sim_nao)

gorjetas.head(2)

# vinculando os dados objetidos do comando .map substituimos os dados contidos no df
gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)

gorjetas.head(5)

gorjetas.dia_da_semana.unique()

dias = {
    'Sun' : 'Domingo', 
    'Sat' : 'Sábado', 
    'Thur' : 'Quinta', 
    'Fri' : 'Sexta'
}

gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias)

gorjetas.head()

gorjetas.hora_do_dia.unique()

hora = {
    'Dinner' : 'Jantar', 
    'Lunch' : 'Almoço'
}

gorjetas.hora_do_dia = gorjetas.hora_do_dia.map(hora)

gorjetas.head()

"""# Importando o Seaborn

"""

# comando para instalar o seaborn
!pip install seaborn==0.9.0

# importando o seaborn, importante anteriormente importar o pandas
import pandas as pd
import seaborn as sns

!pip show seaborn

"""# Análise 1 - Valor da conta e gorjeta"""

gorjetas.columns

valor_gorjeta = sns.scatterplot(x='valor_da_conta', y='gorjeta', data=gorjetas)

"""**Visualmente, o valor da gorjeta aumenta conforme aumenta o valor da conta**"""

# verificando se o df possui valores nulos
print('A base de dados contém {} registros \n'.format(gorjetas.shape[0]))
print('Registros não nulos')
gorjetas.count()

"""## Criando o campo porcentagem"""

gorjetas.head()

gorjetas['porcentagem'] = gorjetas['gorjeta'] / gorjetas['valor_da_conta']

gorjetas.head(2)

gorjetas.porcentagem = gorjetas.porcentagem.round(2)

gorjetas.head(2)

porcentagem_conta = sns.scatterplot(x='valor_da_conta', y='porcentagem', data=gorjetas)

"""**Visualmente, o valor da conta não é proporcional ao valor da gorjeta**"""

# como .relplot junto do parâmetro kind='line' temos a visualização dos dados em linha
porcentagem_conta_linha = sns.relplot(x='valor_da_conta', y='porcentagem', kind='line', data=gorjetas)

# como .lmplot inserimos uma linha de tendência no gráfico de dispersão
sns.lmplot(x='valor_da_conta', y='porcentagem', data=gorjetas)

"""# Análise 2 - Sobremesa"""

gorjetas.head()

# o comando .describe() fornece um conjunto consolidado de indicadores sobre um df ou sobre um df filtrado
gorjetas[gorjetas.sobremesa == 'Sim'].describe()

gorjetas[gorjetas.sobremesa == 'Não'].describe()

sns.catplot(x='sobremesa', y='gorjeta', data=gorjetas)

# utilizando o .relplot com o parâmetro hue podemos criar um gráfico com legendas com os dados dispostos por diferentes grupos
sns.relplot(x='valor_da_conta', y='gorjeta', hue='sobremesa', data=gorjetas)

# com o comando .relplot e a utilização do parâmetro col podemos dividir a visualização dos dados em grupos diferentes e gráficos separados
sns.relplot(x='valor_da_conta', y='gorjeta', hue='sobremesa', col='sobremesa', data=gorjetas)

sns.relplot(x='valor_da_conta', y='gorjeta', col='sobremesa', data=gorjetas)

# com o comando .lmplot inserimos uma linha de têndencia no gráfico
sns.lmplot(x='valor_da_conta', y='gorjeta', col='sobremesa', hue='sobremesa', data=gorjetas)

sns.lmplot(x='valor_da_conta', y='porcentagem', col='sobremesa', hue='sobremesa', data=gorjetas)

# com o parâmetro kind='line' transformamos o gráfico em linha
sns.relplot(x='valor_da_conta', y='porcentagem', col='sobremesa', hue='sobremesa', kind='line', data=gorjetas)

"""**Visualmente, existe uma diferença no valor da gorjeta daqueles que pediram sobremesa e não pediram sobremesa**

## Teste de hipótese

**H<sup>null</sup>**
>**A distribuição da taxa da gorjeta é a mesma nos dois grupos**

**H<sup>alt</sup>**
>**A distribuição da taxa da gorjeta não é a mesma nos dois grupos**
"""

# importando a biblioteca ranksums
from scipy.stats import ranksums

# query para buscar a porcentagem de todos que pediram sobremesa
sobremesa = gorjetas.query("sobremesa == 'Sim'").porcentagem

# query para buscar a porcentagem de todos que não pediram sobremesa
sem_sobremesa = gorjetas.query("sobremesa == 'Não'").porcentagem

r = ranksums(sobremesa, sem_sobremesa)

print('O valor do p-value é {}'.format(r.pvalue))

"""**H<sup>null</sup>**
>**A distribuição da taxa da gorjeta é a mesma nos dois grupos**

# Análise 3 - Dia da semana
"""

gorjetas.head()

gorjetas.dia_da_semana.unique()

# com o .catplot criamos um gráfico agrupado por categorias
sns.catplot(x='dia_da_semana', y='valor_da_conta', data=gorjetas)

sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', data=gorjetas)

sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', data=gorjetas)

sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)

sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)

sns.lmplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)

media_geral_gorjetas = gorjetas.gorjeta.mean()

print('A média geral das gorjetas é de {}'.format(media_geral_gorjetas))

# com o comando .groupby criamos uma visão do df agrupado por um campo específico. O .mean foi utilizado para buscar a média dos resultados do grupo
orjetas.groupby(['dia_da_semana']).mean()

# especificando entre colchetes duplos filtramos/reordenamos colunas as colunas no df 
gorjetas.groupby(['dia_da_semana']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']]

# com o comando .value_counts montamos uma series com a frequência dos registros no df
print('Frequência dos dias')
gorjetas.dia_da_semana.value_counts()

"""## Teste de hipótese

**H<sup>null</sup>**

>**A distribuição do valor da conta é igual no sábado e no domingo**

**H<sup>alt</sup>**

>**A distribuição do valor da conta não é igual no sábado e no domingo**
"""

valor_conta_domingo = gorjetas.query("dia_da_semana == 'Domingo'").valor_da_conta

valor_conta_sabado = gorjetas.query("dia_da_semana == 'Sábado'").valor_da_conta

r2 = ranksums(valor_conta_domingo, valor_conta_sabado)
print('O valor do pvalue é {}'.format(r2.pvalue))

"""**H<sup>null</sup>**

>**A distribuição do valor da conta é igual no sábado e no domingo**

# Análise 4 - Hora do dia
"""

gorjetas.head()

gorjetas.hora_do_dia.unique()

sns.catplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)

# com o parâmetro kind='swarm' temos uma distribuição dos pontos mais espalhada
sns.catplot(x='hora_do_dia', y='valor_da_conta', kind='swarm', data=gorjetas)

# comando .violinplot gera um gráfico de área da dispersão dos resultados em Y e X
sns.violinplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)

# com o comando .boxplot temos um gráfico de área que mostra também uma linha de média entre os dois dados
sns.boxplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)

almoco = gorjetas.query("hora_do_dia == 'Almoço'").valor_da_conta

# com o comando .displot montamos um gráfico de histograma no seaborn
sns.distplot(almoco)

# com o parâmetro kde=False ocultamos a linha de média
sns.distplot(almoco, kde=False)

jantar = gorjetas.query("hora_do_dia == 'Jantar'").valor_da_conta

sns.distplot(jantar)

sns.distplot(jantar, kde=False)

gorjetas.groupby(['hora_do_dia']).mean()

gorjetas.groupby(['hora_do_dia']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']]

"""## Teste de hipótese

**H<sup>null</sup>**

>**A distribuição do valor da conta é igual no jantar e no almoço**

**H<sup>alt</sup>**

>**A distribuição do valor da conta não é igual no jantar e no almoço**
"""

r2 = ranksums(jantar, almoco)

print('O valor do p-value é de {}'.format(r2.pvalue))

"""**H<sup>alt</sup>**

>**A distribuição do valor da conta não é igual no jantar e no almoço**

## Teste de hipótese 2

**H<sup>null</sup>**

>**A distribuição da taxa da gorjeta é igual no jantar e no almoço**

**H<sup>alt</sup>**

>**A distribuição da taxa da gorjeta não é igual no jantar e no almoço**
"""

porcentagem_almoco = gorjetas.query("hora_do_dia == 'Almoço'").porcentagem

porcentagem_jantar = gorjetas.query("hora_do_dia == 'Jantar'").porcentagem

ranksums(porcentagem_almoco, porcentagem_jantar)

r3 = ranksums(porcentagem_almoco, porcentagem_jantar)
print('O valor do p-value é de {}'.format(r3.pvalue))

"""**H<sup>null</sup>**

>**A distribuição da taxa da gorjeta é igual no jantar e no almoço**
"""

