def greeting(name):
  print("Hello, " + name)

class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def greeting(self):
        print("The", self.name, "is", self.color)