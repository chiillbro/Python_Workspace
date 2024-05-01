class Granny:
    def gdisplay(self):
        print("granny")
class Parent(Granny):
    def pdisplay(self):
        print("parent")
class Child(Parent):
    def cdisplay(self):
        print("child")
c=Child()
c.gdisplay()
c.pdisplay()
c.cdisplay()