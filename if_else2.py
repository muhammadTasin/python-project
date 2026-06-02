print ("Dear students customer please input ur billing amount ")
amount = int(input())

if  amount>= 2000 :
    print (f" please pay {(amount*5/100)} tk more")
elif amount >=3400:
    print (f" please pay {(amount*7/100)} tk more")
elif amount>=0 and amount <=1000 :
    print (f" dear customer you don't have to pay any extra Charge, Thank you")
else :
    print (f" you have to pay {amount *22/100} tk more")
