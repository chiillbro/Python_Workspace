class father:
    def pdisplay(self):
        print("parent")
class mother:
    def mdisplay(self):
        print("mother")
class child(father,mother):
    def cdisplay(self):
        print("child")
object=child()
object.cdisplay()
object.pdisplay()
object.mdisplay()