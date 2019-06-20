import json

try:
    f = open("C:\\xampp\\htdocs\\test\\JSON_demo.txt", "r")
except:
    print("Something went wrong")
finally:
    print("File opened successfully")
    f.close()

with open("C:\\xampp\\htdocs\\test\\JSON_demo.txt", "r") as json_file:
    data = json.load(json_file)
    for e in data["employees"]:
        print("Name: " + e["lastName"])
json_file.close()