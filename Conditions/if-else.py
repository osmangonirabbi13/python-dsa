x = 15

if x > 15:
    print('Number is greater then 15')
elif x == 15:
    print("Number is equal to 15")
else:
    print('Number is less then 15')

##Nasted Conditions

y = 4 

if x > 5 : 
    print("x is greater than 5")

    if x % 2 :
        print("x is also even")
    else :
        print("X is Odd")
else:
    print(" X is less than , so not claculating even or odd")


## Ternary Operator

num = -1

result = " postive " if num >= 0 else "Negative"

print("Number is " , result)