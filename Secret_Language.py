m=input("Enter the message:")
print("*******************************************************")
print("Do you want to Encode or Decode?")
x=input("Enter (Encode or Decode):")
if(x=="Encode" or x=="encode"):
   print("*******************************************************")
   print("Encoding Message")
   print("*******************************************************")
   if(len(m)>=3):
     a=input("Enter any random 3 character for starting:")
     b=input("Enter any random 3 character for ending:")
     enc=a+m[1:]+m[0]+b
     print(f"Encoded message={enc}")  
   else:
     enc=m[::-1]
     print(f"Encoded message={enc}")
elif(x=="Decode" or x=="decode"):
    print("*******************************************************")
    print("Decoding Message")
    print("*******************************************************")
    if(len(m)>=3):
       dec=m[-4]+m[3:-4]
       print(f"Decoded message={dec}")
    else:
       dec=m[::-1]
       print(f"Decoded message={dec}")
