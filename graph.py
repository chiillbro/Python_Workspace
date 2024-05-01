class Graph:
 
   def __init__(self,size):
     self.adj=[]
     for i in range(0,size):
       self.adj.append([0 for i in range(0,size)])
       self.size=size

   def add_edge(self,org,des):
      if org>self.size or des>self.size or org<0 or des<0:
         print("Trying to add an invalid edge! (%d,%d)"%(org,des))
      else:
         self.adj[org-1][des-1]=1
         self.adj[des-1][org-1]=1
   
   def remove_edge(self,org,des):
     if org>self.size or des>self.size or org<0 or des<0:
         print("Trying to remove an invalid edge! (%d,%d)"%(org,des))
     else:
          self.adj[org-1][des-1]=0
          self.adj[des-1][org-1]=0
   
   def display(self):
       for row in self.adj:
        print()
        for val in row:
          print("{:4}".format(val),end='')



G=Graph(7)
G.add_edge (1,5)
G.display ()

G.remove_edge (1,5)
G.display ()