import random

def guess_the_number():
  """Plays a number guessing game with the user."""
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  attempts = 0

  while True:
    guess = int(input("Make a guess: "))
    attempts += 1

    if guess < answer:
      print("Too low.")
    elif guess > answer:
      print("Too high.")
    else:
      print(f"You got it! The answer was {answer}. You took {attempts} attempts.")
      break

guess_the_number()
