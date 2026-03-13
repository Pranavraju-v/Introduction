actual_price=float(input("Enter the actual price: "))
selling_price=float(input("Enter selling price: "))
if selling_price>actual_price:
   profit=selling_price-actual_price
   print("Your profit is", profit)
else:
    print("You have no Profit")