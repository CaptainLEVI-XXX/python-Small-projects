import random
number=random.randint(1,100)
print(f"the number is {number}")
usernumber=int(input("guess a number between 1 t0 100   "))
c=1
while(usernumber!=number):
    if(number>usernumber):
        print(f"AHHan guess a larger number {usernumber}")
    elif(number<usernumber):
        print(f"guess a smaller number {usernumber}")  
    usernumber=int(input("GUESS-->    "))
    c=c+1
print(f"you made {c} guesses to get the right answer")