movies=["toy story","soul","happy new year","baby's day out"]
import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')
print("Welcome to my game!")

choose=random.choice(movies)
listm=[]
lives=6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
      =========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for i in choose:
    listm+="_"
    

while "_" in listm:
    user=input("Guess a letter ")
    userr=user.lower()
    for i in range(len(choose)): 
        letter=choose[i]
        if letter == userr:
            listm[i]=letter
            print("Good job")
    if userr not in choose:
        lives-=1
        print("no way! you lose a life")
        print(stages[lives])
        if lives==0:
            print("you lose")
            
        
        
   
    print(listm)