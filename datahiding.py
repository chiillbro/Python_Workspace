class example:
    __a=100   # a is private by prefixing with 2 underscores
    b=200
    print(__a)   #can operate private variable within the class
    def __display(self):     #method display() is private by prefixing with 2 underscores
        print("display")
    def show(self):
        self.__display()   # using a public method to show a private method
object=example()
print(object.b)
object.show()