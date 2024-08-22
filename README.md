# WebScraping-house-of-fraser-
# Descrição do Projeto: 
# Web Scraping e Exportação de Dados para Excel.

## Visão Geral

Este projeto realiza a extração de dados de produtos de um site de e-commerce utilizando técnicas de web scraping e, em seguida, salva as informações coletadas em um arquivo Excel no formato `.xlsx`. O site alvo é a página de "Hoodies and Sweatshirts" da House of Fraser.

## Funcionalidades

### Coleta de Dados

- Realiza uma requisição HTTP para a página de produtos usando a biblioteca `httpx`.
- Analisa o conteúdo HTML retornado utilizando a biblioteca `BeautifulSoup`.
- Extrai informações relevantes dos produtos, incluindo marca, nome e preço.

### Processamento de Dados

- Os dados extraídos são processados e organizados em um formato estruturado.
- Os dados de cada produto são armazenados em um dicionário, que é então convertido em um DataFrame do `pandas`.

### Exportação de Dados

- O DataFrame contendo os dados dos produtos é exportado para um arquivo Excel no formato `.xlsx` usando a biblioteca `openpyxl`.

### Tratamento de Erros

- Implementa tratamento de erros para garantir que quaisquer problemas durante a extração de dados ou a criação do arquivo Excel sejam capturados e relatados.

## Tecnologias Utilizadas

- **`httpx`**: Para realizar requisições HTTP e obter o conteúdo da página web.
- **`BeautifulSoup`**: Para analisar e extrair dados do HTML da página.
- **`pandas`**: Para manipulação e estruturação dos dados em formato tabular.
- **`openpyxl`**: Para exportar os dados para um arquivo Excel no formato `.xlsx`.

## Estrutura do Código

### Função `extract_product_data(product)`

- **Descrição**: Extrai informações de cada produto a partir de um objeto `BeautifulSoup`.
- **Retorno**: Um dicionário com dados do produto (marca, nome e preço).

### Função `upload_to_xlsx(df, output_file)`

- **Descrição**: Exporta o DataFrame contendo os dados dos produtos para um arquivo Excel no formato `.xlsx`.
- **Parâmetros**:
  - `df` (pandas.DataFrame): O DataFrame a ser exportado.
  - `output_file` (str): O nome do arquivo Excel de saída.

### Função `main()`

- **Descrição**: Orquestra o processo de web scraping e exportação de dados.
- **Passos**:
  - Faz a requisição à página.
  - Analisa o HTML.
  - Extrai os dados dos produtos.
  - Salva os dados em um arquivo Excel.
