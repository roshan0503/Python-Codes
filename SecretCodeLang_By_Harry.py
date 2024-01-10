m=input("Enter the message:")
words=m.split(" ")
print("*******************************************************")
print("Do you want to Encode or Decode?")
x=input("Enter (Encode or Decode):")
if(x=="Encode" or x=="encode"):
   print("*******************************************************")
   print("Encoding Message")
   print("*******************************************************")
   nwords=[]
   for word in words:
    if(len(word)>=3):
      a="poi"
      b="jhg"
      enc=a+word[1:]+word[0]+b
      nwords.append(enc)
    else:
      nwords.append(word[::-1])
   print(" ".join(nwords))
      
elif(x=="Decode" or x=="decode"):
    print("*******************************************************")
    print("Decoding Message")
    print("*******************************************************")
    nwords=[]
    for word in words:
      if(len(word)>=3):
        stnew=word[3:-3]
        stnew=stnew[-1]+stnew[:-1]
        nwords.append(stnew)
      else:
        nwords.append(word[::-1])
    print(" ".join(nwords))
