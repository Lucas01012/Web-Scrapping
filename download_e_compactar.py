import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL do site da ANS
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para salvar os PDFs
download_dir = "data/"

# Nome do arquivo zip final
zip_file_name = "anexos.zip"

# Função para baixar os PDFs
def download_pdf(pdf_url, file_name):
    print(f"Baixando: {file_name}")
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, file_name), 'wb') as f:
            f.write(response.content)
            print(f"{file_name} baixado com sucesso!")
    else:
        print(f"Erro ao baixar {file_name}")

# Função para compactar os PDFs em um arquivo ZIP
def compactar_em_zip(pdf_files, zip_name):
    with ZipFile(zip_name, 'w') as zipf:
        for pdf in pdf_files:
            zipf.write(pdf, os.path.basename(pdf))
            print(f"{pdf} adicionado ao arquivo ZIP.")
    print(f"Todos os arquivos foram compactados em {zip_name}!")

# Criando o diretório de downloads se não existir
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Baixando os PDFs
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando todos os links de PDF na página
pdf_links = soup.find_all('a', href=True)
pdf_files = []

# Filtrando e baixando apenas os Anexos I e II
for link in pdf_links:
    pdf_url = link['href']
    if pdf_url.endswith('.pdf') and ("Anexo I" in link.text or "Anexo II" in link.text):
        # Criando nome do arquivo
        file_name = pdf_url.split('/')[-1]
        pdf_files.append(os.path.join(download_dir, file_name))

        # Baixando o arquivo PDF
        if not pdf_url.startswith('http'):
            pdf_url = "https://www.gov.br" + pdf_url
        download_pdf(pdf_url, file_name)

# Compactando os arquivos PDF baixados
compactar_em_zip(pdf_files, zip_file_name)
