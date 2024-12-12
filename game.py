import random
number=random.randint(1,10)
name=input("what is your name?")
print("hello",name,"you get 3 chances to guess a number so be careful and guess correctly")
numguess=0
while numguess<3:
  numguess+=1
  guess=int(input("enter your guess"))
  if guess<number:
    print("go a little higher")
  if guess>number:
    print("go a little lower")
  if guess==number:
    break

if guess==number:
  print("you are correct")
else:
  print("sorry the number is ",number)
