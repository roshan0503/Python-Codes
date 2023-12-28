x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))
y1=float(input("Enter y1: "))
y2=float(input("Enter y2: "))
if(x2-x1==0):
  print("Veritcal line")
else:
  slope=((y2-y1)/(x2-x1))
  print(slope)
  if(slope>0):
    print("positive slope")
  elif(slope<0):
    print("negative slope")
  elif(slope==0):
    print("Horizontal line")
  else:
    print("Invalid input")
