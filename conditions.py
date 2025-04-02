x=float(input("Enter the value of x:"))
y=float(input("Enter the value of y:"))

if x!=y:
  if x>y:
    print("x is greater than y")
  else:
    print("y is greater that x")
else:
  print("Both the numbers are equal")
print("\n")
print("The actual inputs from user are:",x,y, ",Where x is {} and y is {}. ".format(x,y))
