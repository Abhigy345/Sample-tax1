import math
price = float(input("Enter the price of the product:  "))
discount = float(input("Enter the discount offered on that product: "))
def GST(price):
    if price > 0 and price < 1000:
        tax = 0.05
        discounted_price = price - (price * discount)
        tax_amount = discounted_price * tax
        final_price = discounted_price + tax_amount
        return final_price
    
    elif price > 1000 and price < 50000:
        tax = 0.18
        discounted_price = price - (price * discount)
        tax_amount = discounted_price * tax
        final_price = discounted_price + tax_amount
        return final_price
    
    elif price >= 50000:
        tax = 0.28
        discounted_price = price - (price * discount)
        tax_amount = discounted_price * tax
        final_price = discounted_price + tax_amount
        return final_price 
    
print( "the total price of the product is :  $" + str(GST(price)))
        
        