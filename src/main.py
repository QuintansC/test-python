from src.read import managementPDF, alterarCSV
from src.webscrapping import scrapp
import os.path

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

if not os.path.isfile('./docs/anexoI.pdf'):
    scrapp(url)

if not os.path.isfile('./output/anexoI.csv'):
    managementPDF("./docs/anexoI.pdf")

if os.path.isfile('./output/anexoI.csv'):
    alterarCSV('./output/anexoI.csv')