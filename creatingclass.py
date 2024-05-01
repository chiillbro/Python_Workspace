class Human:
   def __init__(self,name,color):
       self.name=name
       self.color=color
   def sleep(self):
       print(self.name+" " +"is sleeping")
   def walk(self):
       print(self.name+" " +"is walking") 
       
human=Human("siva","fair")
print(human.name,human.color)
human.sleep()
human.walk()