from abc import ABC,abstractmethod
class parent(ABC):      #Abstract Class
    @abstractmethod       #Abstract method
    def display(self):
        None
    @abstractmethod
    def show(self) :
        None
class child(parent):     #Concrete Class
    def display(self):
        print("ok")
    def show(self):
        print("no")
object=child()
object.display()
object.show()