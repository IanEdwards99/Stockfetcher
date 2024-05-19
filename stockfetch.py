import matplotlib.pyplot as plt
import yfinance as yf
from consolemenu import *
from consolemenu.items import *

#Example code to fetch stock information and plot it:

    # data = yf.download("AAPL", start="2020-01-01", end="2021-01-01") #Add interval = "1wk" to specify data in intervals of a week.
    # print(data.head())
    # data = yf.download("AAPL", period="5d") #Specify data period.
    # print(data)

    # apple = yf.Ticker("AAPL") #Get generic info data for stock.
    # print(apple.info)

    # multi_tickers = yf.download(["AAPL", "MSFT"], start="2020-01-01", end="2021-01-01") #Obtain data for multiple stocks at once.


    # data = yf.download("AAPL", start="2024-01-01", end="2024-05-19")
    # data['Close'].plot()
    # plt.title("Apple Stock Prices")
    # plt.show()

# fetch multiple tickers in parallel with multithreading using yahooquery.
# https://stackoverflow.com/questions/71161902/get-info-on-multiple-stock-tickers-quickly-using-yfinance

#https://medium.com/@s.sadathosseini/real-time-apple-stock-prices-visualization-using-yfinance-and-streamlit-c4466d0a9b51
def search_stock_execute(): #Make more advanced with searching xml file for stock
    stock_name = input("Please enter a stock name to search for:\n")
    #Replace dates with current date -5 years and current date.
    print(stock_name)
    stock_ticker = yf.Ticker(stock_name)
    historical_prices = stock_ticker.history(period='1d', interval='1m')

    # Clear the plot and plot the new data
    fig, ax = plt.subplots()
    ax.clear()
    ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
    ax.set_xlabel('Time')
    ax.set_ylabel('Stock Value')
    ax.set_title(stock_name + " value")
    ax.legend(loc='upper left')
    ax.tick_params(axis='x', rotation=45)
    fig.show()

def display_top_5():
    print("Top 5 here")


def main():
    menu = ConsoleMenu("Python Stock Ticker", "Read information about your requested stock!")

    # A FunctionItem runs a Python function when selected
    search_stock = FunctionItem("Search for a specific stock", search_stock_execute, should_exit=False)
    top_5 = FunctionItem("Display biggest movers", display_top_5, None)
    menu.append_item(search_stock)
    menu.append_item(top_5)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()
        
if __name__ == '__main__':
    main()
    