class Parent:
    def display(self):
        print("parent")
class son(Parent):
    def sdisplay(self):
        print("son")
class daughter(Parent):
    def gdisplay(self):
        print("daughter")

d=son()
d.display()
d.sdisplay()

c=daughter()
c.display()
c.gdisplay()