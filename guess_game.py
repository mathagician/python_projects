import random  

n=random.randint(1,100)    #in-built function that returns random integer between 1-100

guess_number=int(input("Enter an interger from 1 to 100: "))   

while n!=guess_number:    #taking input untill you guess a right number.
  
  if guess_number<n:
    print("guess higher number than this.")
    guess_number=int(input("Enter an interger from 1 to 100: "))     

  elif guess_number>n:
    print("guess a lower number than this.")
    guess_number=int(input("Enter an interger from 1 to 100: "))

  else:
    break

print("there you go !! you guessed it right.")

#You can always guess a number in maximum 7 guesses.Can you prove how ?




