class demo:
    """def add():   here it will not take this function
         a=100
         b=200"""
    def add(self,a,b,c=300):     #c is default parameter
        print(a+b+c)             #method overloading
object=demo()
object.add(100,200)
object.add(100,300)