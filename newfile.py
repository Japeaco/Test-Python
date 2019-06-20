import os

#create new file
try:
    f = open("C:\\xampp\\htdocs\\test\\pythontest.txt", "x")
except:
    print("Something went wrong")

f.write("\nThis is a new file!")
f.close()

#open and write to new file
try:
    f = open("C:\\xampp\\htdocs\\test\\pythontest.txt", "r")
except:
    print("Something went wrong")

print(f.read())
f.close()

#delete file
if os.path.exists("C:\\xampp\\htdocs\\test\\pythontest.txt"):
    os.remove("C:\\xampp\\htdocs\\test\\pythontest.txt")
else:
    print("Something went wrong")