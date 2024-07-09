import random
number=random.randint(1,100)
# print(number)
while True:
   guess=int(input("guess the number"))
   if guess>number:
       print("guess lower number")
   elif guess<number:
        print("guess highr number")
   else:
      print("congratulation you win")
      break