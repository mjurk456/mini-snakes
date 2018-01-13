minLimit=0
maxLimit=0
step=1 #step for cycle for
# user statistic
fizzes=0
buzzes=0
fizzbuzzes=0
normal=0

#ask user for limits
while True:
    try:
        minLimit,maxLimit=[int(a) for a in input("Input start and stop values for counting dividing them with a space: ").split()]
        break
    except ValueError:
        print("One or all values are wrong. Input should be like 12 10")
#user can input value<0        
if minLimit>maxLimit:
    step=-1    

for i in range(minLimit,maxLimit+step,step):
    if (i%3==0) and (i%5!=0) and (i!=0):
        print("fizz",end=" ")
        fizzes=fizzes+1
    elif (i%5==0) and (i%3!=0) and (i!=0):
        print("buzz",end=" ")
        buzzes=buzzes+1
    elif (i%3==0) and (i%5==0) and (i!=0):
        print("fizzbuzz",end=" ")
        fizzbuzzes=fizzbuzzes+1
    else:
        print(i,end=" ")
        normal=normal+1
print("\nFizzes in range: ", fizzes)
print("Buzzes in range: ", buzzes)
print("Fizzbuzes in range: ",fizzbuzzes)
print("Normal numbers in range: ",normal)
