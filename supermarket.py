price1 = float(input("input the prices of grocery items 1:"))
price2 = float(input("input the prices of grocery items 2:"))
price3 = float(input("input the prices of grocery items 3:"))
grocerylist = [price1, price2, price3]
totalprice= sum(grocerylist)

if( totalprice >= 100 ):
    discount=((10/100)*totalprice)
    finalprice= totalprice - discount
elif ( totalprice >= 50 and totalprice < 100):
    discount = ((5/100)*totalprice)
    finalprice= totalprice - discount
elif( totalprice < 50):
    discount = "No discount"
    finalprice = totalprice
print("Your Bill:")
print("Your Total Price", totalprice)
print("Your Total Discount:", discount)
print("Your Final price:", finalprice)