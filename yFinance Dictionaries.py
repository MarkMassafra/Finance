import yfinance as yf

def print_200d_moving_average(stock_symbol):
    """
    Prints the two hundred day moving average for the given stock symbol.
    """
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

        # Check if the key exists in the info dictionary
        if 'twoHundredDayAverage' in stock_info:
            two_hundred_day_avg = round(stock_info['twoHundredDayAverage'], 2)
            print(f"200-Day Moving Average for {stock_symbol}: {two_hundred_day_avg}")
        else:
            print(f"200-Day Moving Average data not available for {stock_symbol}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
print_200d_moving_average("MSFT")
