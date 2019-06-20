#test
print("hello world!")

#variables
w = 1.8
x = 5
y = 7
z = "awesome"
#casting
cw = float(1.8)
cx = int(5)

#indentation is required
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")


#print type of variable
print(type(z))
print("Python is " + z)

#get position in string and length
print(z[0:3], ", ", len(z))
print(z.upper())

#input example
#print("enter name")
#x = input()
#print("hello, ", x)

#list and for loop
list = ["apple", "banana", "orange"]
list[2] = "pear"
list.append("cherry")
list.insert(1, "peach")
print("\nlength: ", len(list))
for q in list:
    print(q)
if "apple" in list:
    print("Yes, 'apple' is in the fruits list")

print("\ncopy of list: ")
listcopy = list.copy()
listcopy.remove("banana")
del listcopy[2]
for q in listcopy:
    print(q)

print("\nsorted list: ")
list.sort()
for q in list:
    print(q)

#like lists, but unchangeable
thistuple = ("apple", "banana", "cherry")

#like lists, but unordered and unindexed
print("\nset: ")
thisset = {"apple", "banana", "cherry"}
thisset.add("peach")
thisset.update(["cherry", "orange"])
for q in thisset:
    print(q)

#dictionaries are collections
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print("\nDictionary: \n", dict)
m = dict.get("model")
print(m)
#change value
dict["year"] = "2019"
#add new value
dict["color"] = "blue"
#loop through keys and values
for x in dict:
  print("key: ", x, ", Value: ", dict[x])
for x, y in dict.items():
    print(x, y)

#while loop
i = 0
while i < 6:
    print(i)
    i += 1
    #stops current iteration of loop and continues next
    if i < 5:
        continue
    #breaks the loop
    elif i == 3:
        break

#first number specifices starting value
#second number is number of iterations
#third number is number to increment by
for x in range(2, 30, 3):
    print(x)
else:
    print("finally finished!")

print("hello"[0])
