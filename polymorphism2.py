class parent:
    def transport(self):
        print("cycle is used")
class child(parent):
    def transport(self):
        print("bike is used")   #method overriding
object=child()
object.transport()