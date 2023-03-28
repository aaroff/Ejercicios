# Price input

price=int(input("Enter the desired price:"))

# Discount calculation

if price>0:
    if price<=5000:
        disc=price*0.05
    if price<=1000:
        disc=price*0.12
    if price<=15000:
        disc=price*0.2
    else: disc=price*0.3
subtotal=price-disc

# Total price and discount display

print("The initial amount is", price,)
print("The final amount after applying", disc, "of discount is:", subtotal,)
