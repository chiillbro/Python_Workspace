class Node:
 
   def __init__(self,data,next=None):
     
      self.data=data
      self.next=next

class Sll:

   def __init__(self):
     self.head=None
   
       
   
   def display(self):
      temp=self.head
      while temp:
        print(temp.data,"-->",end=" ")
        temp=temp.next
List=Sll()
node=Node(10)
List.head=node
node1=Node(20)
node.next=node1
node2=Node(30)
node1.next=node2
node3=Node(40)
node2.next=node3

List.display ()