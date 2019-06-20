try:
    f = open("C:\\xampp\\htdocs\\test\\xmltext.txt", "a")
except:
    print("Something went wrong")

f.write("\nThis now has more content!")
f.close()

try:
    f = open("C:\\xampp\\htdocs\\test\\xmltext.txt")
except:
    print("Something went wrong")

print(f.read())