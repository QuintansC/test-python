import tabula
import pandas as pd
from zipfile import ZipFile

def managementPDF(location):
    with open(location, 'rb') as path:
        tabula.convert_into(path, './output/anexoI.csv', output_format='csv', pages='3-181')


def alterarCSV(location):
    df = pd.read_csv(location)

    df["OD"] = df["OD"].replace("OD", "Seg. Odontológico")
    df["AMB"] = df["AMB"].replace("AMB", "Seg. Ambulatorial")
    # df["HCO"] = df["HCO"].replace("HCO", "Seg. Hospitalar Com Obstetrícia")
    # df["HSO"] = df["HSO"].replace("HSO", "Seg. Hospitalar Sem Obstetrícia")
    # df["REF"] = df["REF"].replace("REF", "Plano Referência")
    # df["PAC"] = df["PAC"].replace("PAC", "Procedimento de Alta Complexidade")
    # df["DUT"] = df["DUT"].replace("DUT", " Diretriz de Utilização")

    df.to_csv(location, index=False)

    print("Substituição concluída!")

def zipArchivesDocs():
    with ZipFile('./docs/ArquivoUnico.zip', 'w') as zips:
        zips.write('./docs/anexoI.pdf')
        zips.write('./docs/anexoII.pdf')
    print("Zipagem concluída!")

def zipArchivesCSV():
    with ZipFile('./output/Teste_GustavoQuintans.zip', 'w') as zips:
        zips.write('./output/anexoI.csv')
    print("Zipagem concluída!")