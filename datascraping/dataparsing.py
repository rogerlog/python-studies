doc_html = '''
<html><head><title>Pizza de Dados</title></head>
<body>
<section id="about">
         <div class="user-details">
  <p class='title'> Sobre o Pizza de Dados </p>
  <p> O Pizza de Dados é uma iniciativa de 3 apaixonados por ciência de dados que viviam discutindo assuntos, links e conselhos de carreira. A vontade de aprender mais e compartilhar conhecimento era comum a todos e a ausência de um canal em português para tratar desses temas, levou à ideia de formar o pizza de dados.</p>

  <p> O nome é uma espécie de “homenagem” ao repositório datascience.pizza, que se tornou em pouco tempo uma referência de material de estudos de ciência de dados em português.</p>

  <p> Por ser algo feito de forma simples e leve por pessoas que normalmente se enfiam em muitos projetos ao mesmo tempo, o Pizza de Dados tem 3 regras básicas:</p>

<ol>
    <li>Só vamos fazer isso enquanto estiver divertido para todos;</li>
    <li>Não vamos fazer por pressão (de datas, de publicação, de frequência…);</li>
    <li>Nem todos os pizzaiolos originais devem estar em um episódio.</li>
</ol>

  <p> Esperamos que você se divirta, nos dê feedback e aprenda um pouquinho! </p>
</div>

      </section>
    <div class="header-links">
        <a class="link" href="#about" id="link 1">Sobre</a>
        <a class="link" href="#pizzaiolos" id="link 2">Quem somos</a>
        <a class="link" target="_blank" href="https://medium.com/pizzadedados" id="link 3">Revista</a>
        <a class="link" target="_blank" href="https://podcast.pizzadedados.com/" id="link 4">Episódios</a>
        <a class="link" href="#vemcomagente" id="link 5">Assine</a>
        <a class="link" href="#vemcomagente" id="link 6">Apoie</a>
      </div>
'''

from bs4 import BeautifulSoup

import re

sopa = BeautifulSoup(doc_html, 'html.parser')
type(sopa)

apenas_texto = sopa.get_text()
print(apenas_texto)

sopa.find_all(id="link 4")
sopa.find_all(['ol', 'p'])

l = re.compile('l')
for tag in sopa.find_all(l):
    print(tag.name)

for tag in sopa.find_all(True):
    print(tag.name)

for link in sopa.find_all('a'):
    print(link.get('href'))

sopa.find_all(string=re.compile("ciência"))
