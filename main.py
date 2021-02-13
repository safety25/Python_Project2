import random

true_number = random.randint(1,49)
guess_number = int(input("Enter your guess between 1 and 49 : "))  

life = 5

while True:
    if guess_number == true_number :
        print("You find it!")
        break
    
    elif guess_number < true_number:
        print("Go higher")
        guess_number = int(input("ENter your guess 1 and 49 : "))
        life = life -1

    elif guess_number > true_number:
        print("Go lower")
        guess_number = int(input("ENter your guess 1 and 49 : "))
        life = life -1
    
    if life==0:

        print("You loose :(")
        print("Number was",true_number)
        break


    

    

   