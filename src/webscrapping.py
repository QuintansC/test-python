from bs4 import BeautifulSoup
import requests
import wget

def scrapp (url):

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    links = soup.find_all("a", string=["Anexo II.", "Anexo I."] )

    wget.download(links[0].get('href'), "./docs/anexoI.pdf")
    wget.download(links[0].get('href'), "./docs/anexoII.pdf")