import random
print("please enter your name")

name = input()

secretNumber = random.randint(1, 20)

print("okay " + name + " please make a guess form 1 to 20")


for number in range(1,7):
    guess = int(input())
    if guess > secretNumber:
        print("it's higher, try a lower number")
    elif guess < secretNumber:
        print("it's lower, try something higher")
    else:
        break

if secretNumber == guess:
    print("congratulation" + name + "you made the correct guess in " + str(number) + " guesses")
else:
    print("sorry, you failed to make the correcnt guess the correct guess was " + str(secretNumber))   