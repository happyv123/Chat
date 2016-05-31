class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def length(self):
        return abs((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def get(self):
        return self.x1, self.y1, self.x2, self.y2


p = {}
l = {}
while True:
    com = input("Enter command: ")
    if com == "addp":
        name = input("Enter name: ")
        p = {name: Point(int(input("Enter x: ")), int(input("Enter y: ")))}
    elif com == "exit":
        exit()
    elif com == "getp":
        name = input("Enter name: ")
        try: print(p[name].x, p[name].y)
        except: print("Can't find this name")
    elif com == "addl":
        name = input("Enter name: ")
        l = {name: Line(int(input("Enter x1: ")), int(input("Enter y1: ")), int(input("Enter x2: ")), int(input("Enter y2: ")))}
    elif com == "getl":
        name = input("Enter name: ")
        try:
            print(l[name].get())
        except:
            print("Can't find this name")
    elif com == "help":
        print("help \n addp \n getp \n addl \n getl \n getlen \n exit")
    elif com == "getlen":
        name= input("Enter name: ")
        try:
            print(l[name].length())
        except:
            print("Can't find this name")
    else:
        print("Commanderror, try to repeat, or type 'help'")
