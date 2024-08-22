# WebScraping-house-of-fraser-
# Web Scraping and Data Export to Excel

## Overview

This project performs data extraction from an e-commerce site using web scraping techniques and then saves the collected information into an Excel file in `.xlsx` format. The target site is the "Hoodies and Sweatshirts" page of House of Fraser.

## Features

### Data Collection

- Sends an HTTP request to the product page using the `httpx` library.
- Parses the returned HTML content using the `BeautifulSoup` library.
- Extracts relevant information from the products, including brand, name, and price.

### Data Processing

- Extracted data is processed and organized into a structured format.
- Data for each product is stored in a dictionary, which is then converted into a `pandas` DataFrame.

### Data Export

- The DataFrame containing the product data is exported to an Excel file in `.xlsx` format using the `openpyxl` library.

### Error Handling

- Implements error handling to ensure that any issues during data extraction or Excel file creation are captured and reported.

## Technologies Used

- **`httpx`**: For making HTTP requests and obtaining the content of the web page.
- **`BeautifulSoup`**: For parsing and extracting data from the HTML of the page.
- **`pandas`**: For manipulating and structuring data in tabular format.
- **`openpyxl`**: For exporting data to an Excel file in `.xlsx` format.

## Code Structure

### Function `extract_product_data(product)`

- **Description**: Extracts information from each product based on a `BeautifulSoup` object.
- **Returns**: A dictionary with product data (brand, name, and price).

### Function `upload_to_xlsx(df, output_file)`

- **Description**: Exports the DataFrame containing product data to an Excel file in `.xlsx` format.
- **Parameters**:
  - `df` (pandas.DataFrame): The DataFrame to be exported.
  - `output_file` (str): The name of the output Excel file.

### Function `main()`

- **Description**: Orchestrates the web scraping and data export process.
- **Steps**:
  - Sends a request to the page.
  - Parses the HTML.
  - Extracts product data.
  - Saves the data to an Excel file.
