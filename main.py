import httpx # type: ignore
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore

url = 'https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts'
headers = {
    'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

def extract_product_data(product):
    try:
        name = product.find('span', class_='productdescriptionname').get_text()
        brand = product.find('span', class_='productdescriptionbrand').get_text()
        price = product.find('span', class_='CurrencySizeLarge curprice').get_text().strip()
        
        print(f'''
                Brand: {brand} 
                Name: {name} 
                Price: {price}
              ''')
        
        return {
            'Brand': brand,
            'Name': name,
            'Price': price
        }
        
    except Exception as e:
        print(e)

def upload_to_xlsx(df, output_file):
    try:
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Arquivo Exel '{output_file}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o arquivo Exel: {e}")
        

def main():
    response = httpx.get(url, headers=headers) 
    response_html = response.text

    soup = BeautifulSoup(response_html, 'html.parser')
    products = soup.find_all('div', class_='s-productthumbbox')
    
    for product in products:
        extract_product_data(product)
        
    # fist_product = product[0]
    # import pdb 
    # pdb.set_trace()
    # print(product)

    products_data = []

    for product in products:
        product_data = extract_product_data(product)
        if product_data:
            products_data.append(product_data)

    df = pd.DataFrame(products_data)

    upload_to_xlsx(df, 'products.xlsx')
    
if __name__ == '__main__':
    main()