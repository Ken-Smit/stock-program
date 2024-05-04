#Kenneth Smith 
# 5-2-24
# 8.2
#This program is intended to display stock prices using Python dictionaries

def main():
    # Dictionary of stocks with ticker symbols and prices
    stocks = {
        'AMAT': 204.09,
        'NVDA': 887.23,
        'AMD': 150.60,
        'META': 451.96,
        'PLTR': 23.33,
        'AMZN': 186.24,
        'MARA': 17.52,
        'MSFT': 406.66,
        'TESLA': 181.19,
        'AAPL': 183.38
    }

    # Ask the user to enter a ticker symbol
    ticker_symbol = input("Enter a ticker symbol: ").upper()

    # Check if the entered ticker symbol is in the dictionary
    if ticker_symbol in stocks:
        print("Ticker Symbol:", ticker_symbol)
        print("Stock Price:", stocks[ticker_symbol])
    else:
        print("Ticker symbol '{}' not found.".format(ticker_symbol))

if __name__ == "__main__":
    main()
