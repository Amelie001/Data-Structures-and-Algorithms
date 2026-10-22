# Grocery Store 

products = ["apple", "banana", "bread", "rice", "tomato"]

prices = [0.50, 0.30, 3.50, 3.00, 1.00]

product_name = input("Enter a product name: ").lower()

found = False 

for i in range(len(products)): 
    if products[i] == product_name: 
        print("Product:", products[i])
        print("Price: £", prices[i])
        found = True 
        break 

if found == False: 
    print("Product unavailable.")