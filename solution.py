#Please find the solution code below:

import datetime

gbce = {
    #Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value
    "TEA":["Common",0," ",100],
    "POP":["Common",8," ",100],
    "ALE":["Common",23," ",60],
    "GIN":["Preferred",8,(2/100),100],
    "JOE":["Common",13," ",250],
}

def divident_and_pe(stock,v):
    #calculating divident yield
    if v[0] == "Common":
        divident_yield = v[1]/v[3]
    else:
        divident_yield = (v[2]*v[3])/v[3]
    print("\n" +v[0]+ " Dividend Yield for "+stock+" is "+str(divident_yield))

    #calculating for P/E Ratio
    try:
        print("PE Ratio for "+stock+" is "+ str(v[3]/divident_yield))
    except ZeroDivisionError:
        print("PE Ratio for "+stock+" is "+ str(0))
      
trade_entries = {}

def trade_entry(stock):
    if stock not in trade_entries:
        trade_entries[stock] = []
        trade_entries[stock].append([str(datetime.datetime.now()), 100, "Buy", 100])
    else:
        trade_entries[stock].append([str(datetime.datetime.now()), 90, "Sell", 100])
    return trade_entries[stock]

def volume_weighted_stock_price(stock):
    if stock in gbce:
        traded_price = [100, 90, 95, 80, 75]
        quantity = [200, 100, 100, 125, 300]
        vwsp = sum(map(lambda x, y: x * y, traded_price, quantity)) / sum(quantity)
        print("\nVolume Weighted Stock Price for " + stock + " is " + str(vwsp))
    else:
        print("\nStock Symbol is not found")

def geometric_mean():
    price_product = 1
    for k,v in gbce.items():
        price_product = price_product * v[3]
    
    return price_product**(1/len(gbce))

def main():
    stock_symbol = "POP"

    divident_and_pe(stock_symbol, gbce[stock_symbol])

    print("\nNew trade for " +stock_symbol+ " has been recorded as: ", trade_entry(stock_symbol))    
    print("Additional Trades for " +stock_symbol+ " has been recorded: ", trade_entry(stock_symbol))

    volume_weighted_stock_price(stock_symbol)
    
    print("\nGeometric mean of all stocks is: ",geometric_mean(), "\n")

if __name__ == "__main__":
    main()
