#Please find the code below:

gbce = {
    #Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value
    "TEA":["Common",0," ",100],
    "POP":["Common",8," ",100],
    "ALE":["Common",23," ",60],
    "GIN":["Preferred",8,2/100,100],
    "JOE":["Common",13," ",250],
}

for k,v in gbce.items():  

    divident_yield = v[1]/v[3]  
    print("Dividend Yield for "+k+" is "+str(divident_yield)+"%")

    try:
        print("PE Ratio for "+k+" is "+ str(v[3]/divident_yield))
    except ZeroDivisionError:
        print("PE Ratio for "+k+" is "+ str(0))   