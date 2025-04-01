import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

download_dir = "data/"

zip_file_name = "anexos.zip"

def download_pdf(pdf_url, file_name):
    print(f"Baixando: {file_name}")
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, file_name), 'wb') as f:
            f.write(response.content)
            print(f"{file_name} baixado com sucesso!")
    else:
        print(f"Erro ao baixar {file_name}")

def compactar_em_zip(pdf_files, zip_name):
    with ZipFile(zip_name, 'w') as zipf:
        for pdf in pdf_files:
            zipf.write(pdf, os.path.basename(pdf))
            print(f"{pdf} adicionado ao arquivo ZIP.")
    print(f"Todos os arquivos foram compactados em {zip_name}!")

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

pdf_links = soup.find_all('a', href=True)
pdf_files = []

for link in pdf_links:
    pdf_url = link['href']
    if pdf_url.endswith('.pdf') and ("Anexo I" in link.text or "Anexo II" in link.text):
        file_name = pdf_url.split('/')[-1]
        pdf_files.append(os.path.join(download_dir, file_name))

        if not pdf_url.startswith('http'):
            pdf_url = "https://www.gov.br" + pdf_url
        download_pdf(pdf_url, file_name)

compactar_em_zip(pdf_files, zip_file_name)
