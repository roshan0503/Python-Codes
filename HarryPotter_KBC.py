print("Welcome to KBC Harry Potter Edition")
print("******************************************************************")
questions=[
  ["What is the name of the first Harry Potter movie?","Harry Potter and the Chamber of Secrets","Harry Potter and the Sorcerer's Stone","Harry Potter and the Prisoner of Azkaban","Harry Potter and the Goblet of Fire",2],
  ["Who is Harry's best friend at Hogwarts?","Ron Weasley","Draco Malfoy","Neville Longbottom","Luna Lovegood",1],
  ["What is the name of the school where Harry learns magic?","Eastwood Academy","Durmstrang Institute","Hogwarts School of Witchcraft and Wizardry","Beauxbatons Academy of Magic",3],
  ["What is the primary mode of transportation for wizards in the Harry Potter series?","Brooms","Cars","Portkeys"," Thestral-drawn carriages",1],
  ["Which house does Harry belong to at Hogwarts?","Gryffindor"," Slytherin","Hufflepuff","Ravenclaw",1],
  ["What magical object does Harry inherit from Sirius Black?","The Invisibility Cloak","The Marauder's Map","The Deluminator","The Firebolt",2],
  ["What is the name of the three-headed dog guarding the trapdoor on the third floor of Hogwarts in the first movie?","Fluffy"," Fang","Scrabbers","Norbert",1],
  ["In the Harry Potter series, what is the name of the magical creature that can turn into anyone's deepest fears?","Boggart","Hippogriff","Thestral","Blast-Ended Skrewt",1],
  ["What is the name of the school newspaper edited by Rita Skeeter in Harry Potter and the Goblet of Fire?","The Daily Prophet","The Quibbler","The Hogwarts Times","The Daily Bugle",2],
  ["Who teaches Defense Against the Dark Arts in Harry Potter and the Prisoner of Azkaban?","Professor Snape","Professor McGonagall","Professor Lupin","Professor Lockhart",3],
  ["What is the name of Hagrid's pet dragon in Harry Potter and the Philosopher's Stone (Sorcerer's Stone)?","Buckbeak","Norbert","Smaug","Hungarian Horntail",2],
  ["In the Triwizard Tournament, what magical creatures do champions face in the first task?","Blast-Ended Skrewts","Hungarian Horntail","Mermaids","Acromantulas",2],
  ["What spell does Harry use to summon his broomstick during his first Quidditch match in Harry Potter and the Philosopher's Stone?","Expelliarmus","Accio","Wingardium Leviosa","Lumos",2],
  ["What is the name of the house-elf who is freed when presented with clothes by Harry in Harry Potter and the Chamber of Secrets?","Dobby","Winky","Kreacher","Hokey",1],
  ["What is the name of the train that takes students to Hogwarts School of Witchcraft and Wizardry?","The Knight Bus","The Hogwarts Express","The Nimbus 2000","The Floo Network",1],
  ["Who is the headmaster of Hogwarts School of Witchcraft and Wizardry when Harry first arrives?","Professor Snape","Professor McGonagall","Professor Dumbledore","Professor Flitwick",3]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
money = 0
for i in range(0,len(questions)):
  question=questions[i][0]
  print("Question for Rs.",levels[i])
  print(question)
  print(f"a.{questions[i][1]}         b.{questions[i][2]}")
  print(f"c.{questions[i][3]}         d.{questions[i][4]}")
  reply=int(input("Enter answer(1-4) or 0 for quit: "))
  if(reply==questions[i][5]):
    print("Correct Answer")
    print(f"You Won Rs.{levels[i]}")
    print("******************************************************************")
    if(i==4):
      money=10000
    elif(i==9):
      money=320000
  elif(reply==0):
    print("You Quit")
    money=levels[i-1]
    break
  else:
    print("Wrong Answer")
    break
print(f"Your take home money is Rs.{money}")
  
