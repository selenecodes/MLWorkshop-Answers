import datetime as dt

import matplotlib.pylab as plt
import numpy as np
import pandas_datareader.data as web
import seaborn as sns

sns.set(context='notebook')


def get_stocks_2019(stock):
    """
    Bron: https://www.youtube.com/watch?v=_T0l015ecK4
    """
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2019, 12, 31)

    stocks = web.DataReader(stock, 'yahoo', start, end)['Close']

    # Returns last known price & st. dev. of procentual change
    return stocks[-1], stocks.pct_change().std()


def calc_price(start_price=25, days=100, EPS=0.05):
    prices = np.zeros([days + 1])
    prices[0] = start_price

    for day in range(days):
        prices[day + 1] = prices[day] * (1 + np.random.normal(0, EPS))

    return prices


def calc_all_prices(n=100, start_price=25, days=100, EPS=0.05):
    all_prices = []
    for _ in range(n):
        prices = calc_price(days=days, start_price=start_price, EPS=EPS)
        all_prices.append(prices)
    return all_prices


def plot(data):
    days = len(data[0])
    start_price = data[0][0]
    time = list(np.arange(0, days))

    all_prices = data

    for price in all_prices:
        sns.lineplot(time, price)

    plt.axhline(y=start_price, color='black', linestyle='--', label="Startprijs")
    plt.xlim(0, days)
    plt.ylim(bottom=0)
    plt.title("Monte Carlo Methods")
    plt.xlabel("Tijd [dagen]")
    plt.ylabel("Prijs [€]")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()


def plot_norm_dist(data):
    latest_prices = []

    for price in data:
        latest_prices.append(price[-1])

    sns.distplot(latest_prices, rug=True)
    plt.title(f"Gemiddelde: {np.mean(latest_prices):.2f}, Std.dev.: {np.std(latest_prices):.2f}")
    plt.show()


if __name__ == "__main__":
    last_price, std = get_stocks_2019("IBM")

    all_prices = calc_all_prices(n=100, days=100, start_price=last_price, EPS=std)

    # plot(all_prices)
    # plot_norm_dist(all_prices)
