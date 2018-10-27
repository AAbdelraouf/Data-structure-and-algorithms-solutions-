class Node:

   def __init__(self,data,nextNode=None):

    self.data = data
    self.nextNode = nextNode
        
   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:
# 1- Defining the nead node 
   def __init__(self, head = None):
       self.head = head
       self.size = 0

# 2- Define size function 
   def getSize(self):
       return self.size

# 3- Define addNode function 
   def addNode(self, data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size += 1
        return True

# 4- Define print node function to test out the input and output
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())            