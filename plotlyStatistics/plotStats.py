import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls

from sklearn.preprocessing import StandardScaler

import chart_studio

chart_studio.tools.set_credentials_file(username='jtemporal', api_key='44QHB1wF7FdepdHM7AIx')
#tls.set_credentials_file(username='jtemporal', api_key='44QHB1wF7FdepdHM7AIx')

caminho = 'mtcars.csv'
carros = pd.read_csv(caminho)
carros.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = carros.mpg
mpg.iplot(kind='histogram', filename='histograma-simples')

colunas = ['mpg', 'disp', 'hp']
dados = carros[colunas].values

dados_scaled = StandardScaler().fit_transform(dados)

df = pd.DataFrame(dados_scaled)
df.columns = ['mpg', 'disp', 'hp']

df.iplot(kind='histogram', filename='histograma-multiplo')

df.iplot(kind='histogram', subplots=True, filename='histograms-subplot')

df.iplot(kind='histogram', subplots=True, shape=(3,1), filename='histograms-subplot')

df.iplot(kind='histogram', subplots=True, shape=(1, 3), filename='histograms-subplot')

df.iplot(kind='box', filename='box-plots')

fig = {
    'data': [
        {'x': df.mpg, 'y': df.disp, 'mode':'markers', 'name':'mpg'},
        {'x': df.hp, 'y': df.disp, 'mode':'markers', 'name':'hp'}
    ],
    'layout':{
        'xaxis':{'title':''},
        'yaxis':{'title':'Deslocamento Padronizado'}
    }
}
py.iplot(fig, filename='scatter-plot')