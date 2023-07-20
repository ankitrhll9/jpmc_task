gbce = {
    #Stock Symbol, Type, Last Dividend, Fixed Dividend, Par Value
    "TEA":["Common",0," ",100],
    "POP":["Common",8," ",100],
    "ALE":["Common",23," ",60],
    "GIN":["Preferred",8,2/100,100],
    "JOE":["Common",13," ",250],
}

def geometric_mean():
    price_product = 1
    for k,v in gbce.items():
        price_product = price_product * v[3]
    
    return price_product**(1/len(gbce))

print(geometric_mean())

