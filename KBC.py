Question=["1.What is capital of India?","2.What is the national bird of India?","3.How many states are there in India?","4.What is the name of our Prime Minister?","5.Who wrote our national Anthem?"]
print("Welcome to KBC")
print("...................................................")
print(Question[0])
print("""A.Mumbai
B.Delhi
C.Gujarat
D.Chhenai""")
a=str(input("Enter Your Answer: "))
if a=="B":
  print("Sahi Jawab")
  print("1 Crore Jeetgye")
  print("...................................................")
  print(Question[1])
  print("""A.Peacock
B.Parrot
C.Crow
D.Pigeon""")
  b=str(input("Enter Your Answer: "))
  if b=="A":
    print("Sahi Jawab")
    print("2 Crore Jeetgye")
    print("Total= 3 Crore")
    print("...................................................")
    print(Question[2])
    print("""A.29
B.30
C.18
D.25""")
    c=str(input("Enter Your Answer: "))
    if c=="A":
      print("Sahi Jawab")
      print("3 Crore Jeetgye")
      print("Total= 6 Crore")
      print("...................................................")
      print(Question[3])
      print("""A.Manmohan Singh
B.Rahul Gandhi
C.Narendra Modi
D.Amit Shah""")
      d=str(input("Enter Your Answer: "))
      if d=="C":
        print("Sahi Jawab")
        print("4 Crore Jeetgye")
        print("Total= 10 Crore")
        print("...................................................")
        print(Question[4])
        print("""A.Javed Akhtar
B.Sardar Vallabhbhai Patel
C.Indira Gandhi
D.Rabindranath Tagore""")
        e=str(input("Enter Your Answer: "))
        if e=="D":
          print("Sahi Jawab")
          print("5 Crore Jeetgye")
          print("Total= 15 Crore")
          print("Aap Bante hai KBC ke Vijeta")
          print("............................................................")
          print("Khel Samapt")
          print("............................................................")
        else:
          print("Galat Jawab")
          print("Total= 10 Crore")
          print("Apko yahi se wapas jana hoga")
      else:
        print("Galat Jawab")
        print("Total= 6 Crore")
        print("Apko yahi se wapas jana hoga")
    else:
      print("Galat Jawab")
      print("Total= 3 Crore")
      print("Apko yahi se wapas jana hoga")
  else:
    print("Galat Jawab")
    print("Total= 1 Crore")
    print("Apko yahi se wapas jana hoga")
else:
  print("Galat Jawab")
  print("Apko yahi se wapas jana hoga")
