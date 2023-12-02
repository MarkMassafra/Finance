from data_fetcher import fetch_stock_data
from data_processor import process_data
from data_storage import export_to_excel

def main():

    stock_data = fetch_stock_data()
    processed_data = process_data(stock_date)

    filename = "stock_data.xlsx"
    export_to_excel(processed_data,filename)

if __name__ = "__main__":
    main()


