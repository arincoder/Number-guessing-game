import random
while True:
  print("Welcome to the number guessing game.")
  print("All the best!!")

  print("Enter difficulty:")
  print("1.Easy")
  print("2. Medium")
  print("3. Hard")
  choice = int(input("Please enter your choice(1 to 3): "))
  if choice == 1:
    no_attempts = 10
  elif choice == 2:
    no_attempts = 7
  else:
    no_attempts = 5
  tries = 0
  secret_number = random.randint(1,100)
  for i in range(no_attempts):
      guess = int(input("Guess a number between 1 and 100 inclusive: "))
      tries += 1
      if guess == secret_number:
        print("Congratulations. You guessed the number!!")
        print(f"you took {tries} attempt(s)")
        break 
      if guess < secret_number:
          print("Not quite. Think higher")
      elif guess > secret_number:
          print("Not quite. Think lower")
  else:
    print("Game over.")
    print(f"the correct number is {secret_number}")
    print(f"you took {tries} attempt(s)")

  replay = input("Do you want to play again(yes/no)?")
  if replay != "yes":
    break
