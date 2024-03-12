
def factorial(x):

    if x == 1:
        return 1
    else:
        
        return (x * factorial(x-1))

num = int(input("Enter a number: "))

result = factorial(num)
print("The factorial of", num, "is", result)



def calculation():
    number1 = int(input("num 1"))
    number2 = int(input("num 2"))
    return (number1 + number2)
    

total = calculation()

print(total)


