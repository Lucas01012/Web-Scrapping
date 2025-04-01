# 📂 Download e Compactação de PDFs da ANS

Este script Python baixa arquivos PDF específicos (Anexo I e Anexo II) de uma página da web da Agência Nacional de Saúde Suplementar (ANS) e os compacta em um arquivo ZIP.

## Descrição

O script realiza as seguintes tarefas:

1. **Extrai Links PDF:** Extrai todos os links da página web especificada.
2. **Filtra PDFs:** Filtra os links para encontrar apenas aqueles que terminam com `.pdf` e contêm "Anexo I" ou "Anexo II" no texto do link.
3. **Download dos PDFs:** Baixa os arquivos PDF encontrados e os salva em um diretório local chamado `data/`.
4. **Compactação em ZIP:** Compacta todos os arquivos PDF baixados em um arquivo ZIP chamado `anexos.zip`.

## Pré-requisitos

Certifique-se de que você tenha o **Python 3** instalado em seu sistema. Além disso, você precisará instalar as seguintes bibliotecas Python:

```bash
pip install requests beautifulsoup4
Como Usar
1. Clone o Repositório (Opcional)
Se você estiver usando o Git, clone este repositório para o seu computador:

bash
Copiar
git clone https://github.com/seu-usuario/seu-repositorio.git
2. Execute o Script
Navegue até o diretório onde o script está localizado e execute-o usando o Python:

bash
Copiar
python download_e_compactar.py
3. Resultados
Após a execução, os arquivos PDF serão baixados para o diretório data/ e um arquivo ZIP chamado anexos.zip será criado no diretório raiz do projeto.

Estrutura do Diretório
graphql
Copiar
seu_projeto/
├── download_e_compactar.py   # Script Python principal
├── data/                     # Diretório onde os PDFs são baixados
│   ├── Anexo I.pdf           # Anexo I baixado
│   └── Anexo II.pdf          # Anexo II baixado
└── anexos.zip                # Arquivo ZIP contendo os PDFs
Dependências
requests: Para fazer solicitações HTTP.

beautifulsoup4: Para analisar o HTML da página web.

zipfile: Para compactar os arquivos em um arquivo ZIP (biblioteca padrão do Python).

os: Biblioteca padrão do Python para criar diretórios.
