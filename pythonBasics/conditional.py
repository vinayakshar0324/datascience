billAmount = int(input("Enter The Bill Amount:"))

if billAmount<500:
    Discount = billAmount * 0.05
    print("Discount Amount is:", Discount)
else:
    Discount = billAmount*0.10
    print("Discount Amount is:", Discount)
    
print("Your final Amount is:", billAmount-Discount)
