from bs4 import BeautifulSoup

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
        <a class="link" href="#about" data-scroll="">Sobre</a>
        <a class="link" href="#pizzaiolos" data-scroll="">Quem somos</a>
        <a class="link" target="_blank" href="https://medium.com/pizzadedados">Revista</a>
        <a class="link" target="_blank" href="https://podcast.pizzadedados.com/">Episódios</a>
        <a class="link" href="#vemcomagente" data-scroll="">Assine</a>
        <a class="link" href="#vemcomagente" data-scroll="">Apoie</a>
      </div>
'''

sopa = BeautifulSoup(doc_html, 'html.parser')
print(sopa)

print(sopa.prettify()[0:350])

sopa = BeautifulSoup('<b body="description">O primeiro e o mais querido podcast sobre ciência de dados no Brasil</b>',
                     'html.parser')

tag = sopa.b
type(tag)

print(tag)

tag.name

tag.name = 'podcast'
tag

tag.name

tag['body']

tag.attrs

tag['id'] = 3
tag.attrs

tag

del tag['body']
tag

tag.attrs

sopa = BeautifulSoup(doc_html, 'html.parser')
sopa.head

sopa.title

sopa.body
