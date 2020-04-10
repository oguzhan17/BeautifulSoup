import requests
from bs4 import BeautifulSoup

for sayfa in range(2, 1376):
    sayfa = str(sayfa)
    url = 'https://www.idefix.com/kategori/Kitap/Edebiyat/grupno=00055?Page=' + sayfa
    url = url.strip()
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    link = soup.find_all('a', attrs={'class' : 'product-image'})
    for links in link:

        all_link = 'https://www.idefix.com/'+links.get('href')
        soup = BeautifulSoup(r.content, 'html.parser')

        all_link = all_link.strip()
        url = requests.get(all_link)  # Her gelen link'e istek atıyoruz
        soup = BeautifulSoup(url.content, 'html.parser')
        name = soup.find('h1', attrs={'class': 'mt0'}).text.strip()
        barcode = soup.findAll('a', attrs={'class': 'bold'})
        blen = len(barcode) -1
        isim = barcode[0].text
        barkod = barcode[blen].text
        content = "\"name\"" + ":" + "\"" + isim + "\""    "," + "\""  "barcode" + "\"" + ":"+ "\"" + barkod + "\""
        print(content)

