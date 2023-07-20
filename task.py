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

trade_records = {}

for k,v in gbce.items():  

    divident_yield = v[1]/v[3]  
    print("Dividend Yield for "+k+" is "+str(divident_yield)+"%")

    try:
        print("PE Ratio for "+k+" is "+ str(v[3]/divident_yield))
    except ZeroDivisionError:
        print("PE Ratio for "+k+" is "+ str(0))

    print("Volume Weighted Stock Price for "+k+" is "+str(v[3]))")   

#code to get the current timestamp

# trade_records["TEA"] = [str(datetime.datetime.now()), 100, "Buy", 100]
# trade_records["POP"] = [str(datetime.datetime.now()), 90, "Sell", 100]

# print(trade_records)

