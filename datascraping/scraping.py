import re

from bs4 import BeautifulSoup
from requests import get

r = get('https://pizzadedados.com/')

sopa = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
type(sopa)

print(sopa.prettify()[:100])

for link in sopa.find_all('a'):
    print(link.get('href'))

parametros_busca = {'href': re.compile("^http")}
for link in sopa.find_all('a', attrs=parametros_busca):
    print(link)

file = open('parsed_data.txt', 'w')
for link in sopa.findAll('a', attrs=parametros_busca):
    sopa_link = str(link.get('href'))
    print(sopa_link)
    file.write(sopa_link)
    file.write('\n')
file.flush()
file.close()
