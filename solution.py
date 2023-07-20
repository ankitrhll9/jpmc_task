#Please find the code below:

import datetime

gbce = {
    #Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value
    "TEA":["Common",0," ",100],
    "POP":["Common",8," ",100],
    "ALE":["Common",23," ",60],
    "GIN":["Preferred",8,2/100,100],
    "JOE":["Common",13," ",250],
}

def results(k,v):

    #code for divident yield
    divident_yield = v[1]/v[3]  
    print("\nDividend Yield for "+k+" is "+str(divident_yield)+"%")

    #code for P/E Ratio
    try:
        print("PE Ratio for "+k+" is "+ str(v[3]/divident_yield))
    except ZeroDivisionError:
        print("PE Ratio for "+k+" is "+ str(0))
      
trade_entries = {}

def trade_entry(stock):
    if stock not in trade_entries:
        trade_entries[stock] = []
        trade_entries[stock].append([str(datetime.datetime.now()), 100, "Buy", 100])
    else:
        trade_entries[stock].append([str(datetime.datetime.now()), 90, "Sell", 100])
    return trade_entries[stock]

def geometric_mean():
    price_product = 1
    for k,v in gbce.items():
        price_product = price_product * v[3]
    
    return price_product**(1/len(gbce))

def main():
    stock_symbol = "ALE"

    results(stock_symbol, gbce[stock_symbol])

    print("\nNew trade for " +stock_symbol+ " has been recorded as: ", trade_entry(stock_symbol))    
    #Adding a new trade to the symbol
    print("\nAdditional Trades for " +stock_symbol+ " has been recorded: ", trade_entry(stock_symbol))
    
    print("\nGeometric mean of all stocks is: ",geometric_mean())

if __name__ == "__main__":
    main()
