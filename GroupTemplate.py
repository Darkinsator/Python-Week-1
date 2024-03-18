#functions

int1 = int(input("Enter number 1 :"))
int2 = int(input("Enter number 2 :"))
def newFunction(int1, int2):
    tot = int1 + int2
    return tot

total = newFunction(int1, int2)
print(total)


#operators
int1 = int(input("Enter number 1 :"))
int2 = int(input("Enter number 2 :"))
result = 0

def add(int1, int2):
    tot = int1 + int2
    return tot

def minus(int1, int2):
    tot = int1 - int2
    return tot

def divide(int1, int2):
    tot = int1 / int2
    return tot

def multiply(int1, int2):
    tot = int1 * int2
    return tot

operation = input("Choose an arithmetic operation.(1)Addition,(2)Subtraction,(3)Division,(4)Multiplication :")

if operation == "1":
    result = add(int1, int2)
elif operation == "2":
    result = minus(int1, int2)
elif operation == "3":
    result = divide(int1, int2)
elif operation == "4":
    result = multiply(int1, int2)

print(result)



#classes and objects
class Group:
  def __init__(self, group, week, topic):
    self.group = group
    self.week = week
    self.topic = topic
print(".........................................")
group = input("Enter your group name :")
week = int(input("Enter python learning week :"))
topic = input("What topic are you focusing on :")
print(".........................................")
p1 = Group(group, week, topic)

print("Welcome " + p1.group + " you are in week " + str(p1.week) + " and learning " + topic +".")
print("Keep up the good work " + group +".")





#control flow

#if statement


a = int(input("Enter a value for a :"))
b = int(input("Enter a value for b :"))
if b > a:
  print("b is greater than a")
else:
    print("a is greater than b")

#while loop
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#for loop and data structure

counter = 0
length = input("Enter the array length")
fruits = [None] * int(length)
for x in fruits:
    counter = counter + 1
    fruits[counter-1] = input("Enter position " + str(counter) + " in the array :")

counter = 0
for x in fruits:
  counter = counter + 1
  print("The counter position of the array is " + str(x))


#variable and types
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = 5
print(type(x))