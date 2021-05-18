import pandas as pd
import cufflinks as cf
import plotly.tools as tls
import chart_studio

chart_studio.tools.set_credentials_file(username='jtemporal', api_key='44QHB1wF7FdepdHM7AIx')


#tls.set_credentials_file(username='jtemporal', api_key='44QHB1wF7FdepdHM7AIx')

caminho = 'mtcars.csv'
carros = pd.read_csv(caminho)
carros.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = carros[['cyl', 'wt','mpg']]

layout = dict(title='Gráfico de um DataFrame Pandas',
              xaxis=dict(title='eixo-x'),
              yaxis=dict(title='eixo-y'))

df.iplot(filename='grafico-de-linha', layout=layout)

