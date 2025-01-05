import random
from game_data import data
from art import logo, vs

def format_data(account):
  """Formats account data for display."""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks if the user's guess is correct."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  """Plays the Higher or Lower game."""
  print(logo)
  score = 0
  game_over = False

  account_a = random.choice(data)
  account_b = random.choice(data)

  while not game_over:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
      account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")

game()
