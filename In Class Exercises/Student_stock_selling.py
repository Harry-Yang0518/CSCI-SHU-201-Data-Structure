def stock_buy_sell(prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def main():
    l1 = [7,1,5,3,6,4]
    l2 = [7,6,4,3,2,1] 
    l3 = [2,9,5,2,3,1,2]
    
    print(stock_buy_sell(l1)) # 5
    print(stock_buy_sell(l2)) # 0 
    print(stock_buy_sell(l3)) # 7

if __name__ == '__main__':
    main()