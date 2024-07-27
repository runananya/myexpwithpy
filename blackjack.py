print("Hey there! Do you wanna play blackjack")
import random
print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
""")

choice1=random.randint(0,10)
choice2=random.randint(0,11)
list1=[]
list1.append(choice1)
list1.append(choice2)
print(f"Your Cards:{list1}")

choice3=random.randint(0,10)
print(f"Computer's first card: {choice3}")
choice4=random.randint(0,11)
list2=[]
list2.append(choice3)
list2.append(choice4)
ch=input("Type 'y' to get another card , type 'n' to pass:")
if ch=="y":
      choice5=random.randint(0,10)
      sumuser2=choice1+choice2+choice3
      sumcomp=choice3+choice4
      win=21-sumuser2
      win2=21-sumcomp
      if win<win2:
         print("YOU WIN")
      else:
          print("YOU LOSE")
else:
      sumuser=choice1+choice2
      sumcomp=choice3+choice4
      win=21-sumuser
      win2=21-sumcomp
      if win<win2:
         print("YOU WIN")
      else:
          print("YOU LOSE")

    
    
