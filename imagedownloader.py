import requests
from bs4 import BeautifulSoup
import os

#url = 'https://www.vogue.co.uk/fashion/gallery/menswear-aw23-shows'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    source = soup.find_all('src')
    for source in images:
        print(source{'media'})
