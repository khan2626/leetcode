
def best_time_to_trade_stock(prices):
    buy_price = prices[0]
    profit = 0

    for price in prices[1:]:
        if buy_price > price:
            buy_price = price
        profit = max(profit, price - buy_price)
    return profit

if __name__ == '__main__':
    prices = [7,1,5,3,4]
    print(best_time_to_trade_stock(prices))