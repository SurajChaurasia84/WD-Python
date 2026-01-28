i =1 
while i<=3:
    a=int(input("Enter even number: "))
    if a%2==0:
        break
    i+=1
if i==4:
    print("You lose")
else:
    print("You win")