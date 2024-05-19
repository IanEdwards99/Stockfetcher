import matplotlib.pyplot as plt
import yfinance as yf

def main():
    print("Shtuff")
    data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
    print(data.head())


if __name__ == '__main__':
    main()
    