a=float(input("Enter unit: "))
if(a<=50):
  cost=a*0.50
elif(a>50 and a<=150):
  cost=50*0.50+(a-50)*0.75
elif(a>150 and a<=250):
  cost=50*0.50+100*0.75+(a-150)*1.20
else:
  cost=50*0.50+100*0.75+100*1.20+(a-250)*1.50
tax=(cost*20)/100
bill=cost+tax
print("Amount to be paid: ",cost,"+",tax,"=",bill)
