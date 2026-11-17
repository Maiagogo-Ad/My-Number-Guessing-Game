import random

sec_num = random.randint(1,100)
num_attempts = 0

while True:
    try:
         choice = int(input("Guess a number between 1-100: "))
         if choice > sec_num:
              print("Too High!")
              num_attempts += 1
         elif choice < sec_num:
              print("Too Low!")
              num_attempts += 1
         else:
              print("Congratulations!")
              print(num_attempts)
              break
            
    except ValueError:
         print("Invalid input")
