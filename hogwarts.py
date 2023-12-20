print('Welcome to Hogwarts! You will be asked questions, and your answer will decide the house that you will be assigned to.')

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Question_1= input('Q1) Do you like Dawn or Dusk?\n')   
if Question_1.lower() == 'dawn':
    Gryffindor += 1
    Ravenclaw += 1
elif Question_1.lower() == 'dusk':
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input.')

Question_2= input('Q2) When I’m dead, I want people to remember me as?\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n')   

if Question_2.lower() == 'the good':
    Hufflepuff +=2
elif Question_2.lower() == 'the great':
    Slytherin += 2
elif Question_2.lower() == 'the wise':
    Ravenclaw += 2
elif Question_2.lower() == 'the bold':
    Gryffindor += 2
else:
    print('Wrong input')

Question_3= input('Q)3 Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n')
if Question_3.lower()=='The violin':
  Slytherin+= 4
elif Question_3.lower()== 'The trumpet':
  Hufflepuff+=4
elif Question_3== 'The piano':
  Ravenclaw+= 4
elif Question_3== 'The drum':
  Gryffindor+= 4
else:
  print('Wrong Output')

if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
  print(' Your House is Gryffindor!')
elif Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
  print('Your House is Hufflepuff!')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print('Your House is Ravernclaw!')
else:
  print('Your House is Slytherin!')