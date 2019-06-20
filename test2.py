import json
import mymodule as mm

#functions
def first_function(msg):
    print("\nThis is my first function")
    print(msg)

def numbers(x, y):
    return x + y

def recursion(k):
    if(k>0):
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result

first_function("This is a parameter")
print(numbers(5, 10))
print("\nThis is recursion: ")
recursion(6)

print("\nThis is a lambda function: ")
def lambdafunc(n):
    return lambda a : a * n

myDoubler = lambdafunc(2)
myTripler = lambdafunc(3)

print(myDoubler(11))
print(myTripler(11))

print("\nArray: ")
arr = ["Ford", "Volvo", "BMW"]
for d in arr:
    print(d)

print("\nThis is a class: ")
class Person:
    #intialising object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #creating a function within the class
    def greeting(self):
        print("Hello, my name is", self.name, "and I'm", self.age)

#this is child class for Person
class Student(Person):
    def __init__(self, name, age, university):
        #keeps inheritance of parent class
        Person.__init__(self, name, age)
        self.university = university

    def greeting(self):
        print("Hello, my name is", self.name, "and I'm", self.age,
              "I go to", self.university)

p1 = Person("John", 23)
p2 = Student("James", 24, "Newcastle university")
p1.greeting()
p2.greeting()

print("\nThis is imported from mymodule.py")
mm.greeting("John")

a1 = mm.animal("Monkey", "brown")
a2 = mm.animal("Dolphin", "blue")
a3 = mm.animal("Turtle", "green")

anarr = [a1, a2, a3]

for p in anarr:
    p.greeting()

#JSON
print("\nThis is JSON: ")
x1 = '{"name":"John", "age":"34", "city":"New York"}'
#converts to a python dictionary
y1 = json.loads(x1)
print(y1['age'])

x2 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y2 = json.dumps(x2, indent=2, sort_keys=True, separators=(", "))
print(y2)

#Error handling
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")