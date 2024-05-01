class Node:
 
   def __init__(self,data,next=None):
     
      self.data=data
      self.next=next

class Sll:

   def __init__(self):
     self.head=None
   def in_beg(self,data):
     nb=Node(data)
     nb.next=self.head
     self.head=nb
    
   def in_end(self,data):
     ne=Node(data)
     temp=self.head
     while temp.next:
        temp=temp.next
     temp.next=ne
     
   def in_pos(self,pos,data):
     np=Node(data) 
     temp=self.head
     for i in range(pos-1):
       temp=temp.next
     np.data=data
     np.next=temp.next
     temp.next=np
       
   
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
List.in_beg (5)
List.in_end (50)
List.in_pos (4,35)
List.display ()