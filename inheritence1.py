class parent:
    def __init__(self,c,h):
        self.color=c
        self.height=h
    def run(self):
        print("running .....")
    def eat(self):
        print("eating......")
class child(parent):
    def walk(self):
        print("walking.....")
siva=child("dusky",5.8)
print(siva.color,",",siva.height)
siva.run()
siva.eat()
siva.walk()