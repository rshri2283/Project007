day=input("Enter the day:")
amount=int(input("Enter the amount you shopped for:"))

if day.lower()=="sunday" and amount>=5000:
  discount=(amount*10)/100
  amount=amount-discount
  print("After discount the amount will be:", amount)
else:
  print("Without discount the price will be:", amount)

