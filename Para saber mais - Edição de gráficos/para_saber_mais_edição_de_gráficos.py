import pandas as pd

!pip install seaborn==0.9.0

import pandas as pd
import seaborn as sns

dados = pd.read_csv('tips.csv')

from google.colab import drive
drive.mount('/content/drive')

dados.head()

"""**Inserindo um subtítulo**"""

primeiro_plot = sns.scatterplot(x='total_bill', y='tip', data=dados)

primeiro_plot

primeiro_plot.get_figure()

primeiro_plot.figure.suptitle('Valor da conta x Gorjeta')

primeiro_plot.get_figure()

"""**Inserindo título **"""

primeiro_plot.set_title('Análise do valor da gorjeta em função do valor da conta')

primeiro_plot.get_figure()

primeiro_plot.set(xlabel='Valor da conta', ylabel='Valor da gorjeta')

primeiro_plot.get_figure()

imagem = primeiro_plot.get_figure()

imagem.savefig('imagem.png')