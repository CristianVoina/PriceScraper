from bs4 import BeautifulSoup
from urllib.request import urlopen

content = urlopen("http://www.playbike.ro/produs.php?id_produs=39353").read()

f = open("pagina.txt", "a")
f.write(str(content))
f.close()

#print (content)

soup = BeautifulSoup(content, "html.parser")

pret_oferta = soup.find('span', {'class' : 'pret oferta'})
pret_vechi = soup.find('span', {'class' : 'pret_vechi'})
titlu = soup.find('h1')

#for preturi in spans
print("Titlu: " + titlu.text)
print("Pret Oferta: " + pret_oferta.text)
print("Pret Vechi: " + pret_vechi.text)

#print("Hello World")