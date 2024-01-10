m=input("Enter the message:")
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
print("*******************************************************")
print("Decoding Message")
print("*******************************************************")
if(len(enc)>=3):
  dec=enc[-4]+enc[3:-4]
  print(f"Decoded message={dec}")
else:
  dec=enc[::-1]
  print(f"Decoded message={dec}")
