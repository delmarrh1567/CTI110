#CTI-110
#M5HW2 - Software Sales
#Hasan DelMarr
#22 November 2017


# Defining discount percentage

Sales = int(input("How Many Software Packages will you Purchase?"))
packageAmount = 99


if Sales < 10:
    discount = 0
elif Sales < 20:
    discount = 0.10
elif Sales < 50:
    discount = 0.20
elif Sales < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = Sales * packageAmount
discountAmount = discount * subTotal
total = subTotal - discountAmount

print("Amount of discount: $" + format( discountAmount, ",.2f") +"total amount: $" + format( total, ",.2f"))




        
