
# game by TaaJ
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over
import random


n=random.randint(1,30)
a=1
print("Number of guesses is limited to only 10 chance: ")
while (a<=10):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<n:
        print("you enter less number please input greater number.\n")
    elif guess_number>n:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(a,"no.of guesses he took to finish.")
        break
    print(10-a,"no. of guesses left")
    a = a + 1

if(a>10):
    print("Game Over")
  
