class Node():

 def __init__(self,data):
     
    self.data=data
    self.next=None
    
class SLL():

 def __init__(self):
 
    self.head=None
    
 def display(self):
 
    if self.head==None:
     print("list is empty")
     
    else:
     temp=self.head
     while temp:
      print(temp.data,"-->",end=" ")
      temp=temp.next
 
 def delete_begin(self):
    
    temp=self.head
    self.head=temp.next
    temp.next=None
 
 def delete_end(self):
    
    prev=self.head
    temp=self.head.next
    while temp.next is not None:
      
      
      temp=temp.next
      prev=prev.next
    prev.next=None
 
 def delete_position(self,pos):
    
    prev=self.head
    temp=prev.next
    for i in range(1,pos-1):
     
     prev=prev.next
     temp=temp.next
    prev.next=temp.next
    temp.next=None

L=SLL()
n=Node(10)
L.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
L.delete_begin ()
L.delete_end ()
#L.delete_position (3)
L.display()