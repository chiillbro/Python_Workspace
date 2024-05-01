class Queue:

  def __init__(self ):
    self.items=[]

  def is_empty(self):
    return self.items==[]
   
  def enqueue(self,item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)
  
  def print_queue(self):
     print(self.items)


q=Queue()
print(q.is_empty ())
q.enqueue (6)
q.enqueue ('a')
q.enqueue ('y')
q.enqueue ('y')
print(q.is_empty ())
q.print_queue ()
q.dequeue ()
q.dequeue ()
q.print_queue ()