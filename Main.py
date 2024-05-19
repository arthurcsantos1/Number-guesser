import random
from art import logo

print(logo)



answer = random.randrange(1, 101)

def dificulty_level():
  if dificulty_chosen == "easy":
    return "You have 10 attempts"
  elif dificulty_chosen == "hard":
    return "You have 5 attempts"


print("Welcome to the number Guessing game!")
print("I am thinking of a number between 1 and 100!")
print(f"The correct number is: {answer}")

dificulty_chosen = input("Choose the difficulty, type hard or easy: ")

print(dificulty_level())

player_guess_string = input("Make a guess: ")
player_guess = int(player_guess_string)

should_continue = 0

if dificulty_chosen == "hard":
  should_continue = 5
elif dificulty_chosen == "easy":
  should_continue = 10


def compare_answer():
  global should_continue
  global player_guess
  if player_guess > answer:
    return "Too high!"
  elif player_guess < answer:
    return "Too low!"
  elif player_guess == answer:
    return "YOU GOT IT, CONGRATULATIONS!"
    

while should_continue != 0:
  should_continue -= 1
  if should_continue == 0:
    print ("You lose!")
  elif player_guess == answer:
    print("YOU GOT IT, CONGRATULATIONS!")
    should_continue = 0
  else:
    print(compare_answer())
    player_guess_string = input("Make a guess: ")
    player_guess = int(player_guess_string)
