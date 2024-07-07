import random 
 
a=random.randint(1,100) 
g=0
print("in this game you have to guess a random number wich is in the range of 1 to 100. You will be getting clues after each number you input as a guess")
b=int(input("give a guess"))
if b>100 or b<1:
    print("the number should be in the range of 1 to 100")
g=g+1   
if b==a:
    print("you found the random number wich was",a,"in 1 try")
    quit()
c=(a+10)
d=(a-10)
e=(a+5)
f=(a-5)
if b>=f and b<=e:
        print("you are really close")
else:    
    if b>=d and b<=c:
        print("you are close")
    
    
    if b<a:
        print("try a higher number")
    if b>a:
        print("try a lower number")


while True:
    g=g+1
    b=int(input("give a guess"))
    if b>100 or b<1:
        print("the number should be in the range of 1 to 100")
    if (b == a):
        break
    if b>=f and b<=e:
        print("you are really close")
    else:
        if b>=d and b<=c:
            print("you are close")
    
    if b<a:
        print("try a higher number")
    if b>a:
        print("try a lower number")
print("you found the random number wich was",a,"in ",g,"tries")
