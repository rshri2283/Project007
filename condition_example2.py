day=input("Enter the day of shopping:")
amount=int(input("Enter the amount of total shopping:"))

if day.lower()=="sunday" and amount>=5000 :
    discount=(amount*10)/100
    amount=amount-discount
    print("Total amount after 10% discount is:",amount)
elif day.lower()=="sunday" and amount>=4000 :
    discount=(amount*5)/100
    amount=amount-discount
    print("Total amount after 5% discount is:",amount)

else:
  print("The total amount to be paid is:", amount)
print("\n")
print("Shopping day and amount are as follows:",day,amount)
