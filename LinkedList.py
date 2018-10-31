class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class Linked_List:
    def __init__(self):
        self.Linked_List_Nodes = None
    
    def printNodes(self):
        linkedlist = self.Linked_List_Nodes
        while linkedlist is not None:
            print(linkedlist.data)
            linkedlist = linkedlist.nextNode

list1 = Linked_List()
list1.Linked_List_Nodes = Node("First Node")
list2 = Node("Second Node")
list3 = Node("Thirs Node")
list4 = Node("4th Node")
list1.Linked_List_Nodes.nextNode = list2
list2.nextNode = list3
list3.nextNode = list4
print(list1.printNodes())
# Linked List try number 3 #
# class node:
#     def __init__(self, data = None):
#         self.data = data
#         self.nextNode = None

# class MyLinkedList:
#     def __init__(self):
#         self.Linked_List_Nodes = None

#     def printList(self):
#         while self.Linked_List_Nodes is not None:
#             print(self.Linked_List_Nodes.data)
#             self.Linked_List_Nodes = self.Linked_List_Nodes.nextNode

# list1 = MyLinkedList()
# list1.Linked_List_Nodes = node("First Thing")
# list2 = node("Second Things")
# list1.Linked_List_Nodes.nextNode = list2
# list1.printList()



# class Node:

#     def __init__(self, rootData):

#         self.left = None
#         self.right = None
#         self.rootData = rootData

# # Define insert function #
#     def insert(self, data):
# # Compare the new value with the parent node
#         # If rootData is true/exist
#         if self.rootData:
            
#             if data < self.rootData:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.rootData:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.rootData),
#         if self.right:
#             self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

# root.PrintTree()





# # Singly Linked List #
# class Node:

#    def __init__(self,data ,nextNode = None):

#     self.data = data
#     self.nextNode = nextNode
        
#    def getData(self):
#        return self.data

#    def setData(self,val):
#        self.data = val

#    def getNextNode(self):
#        return self.nextNode

#    def setNextNode(self,val):
#        self.nextNode = val


# class LinkedList:
# # 1- Defining the nead node 
#    def __init__(self, head = None):
#        self.head = head
#        self.size = 0

# # 2- Define size function 
#    def getSize(self):
#        return self.size

# # 3- Define addNode function 
#    def addNode(self, data):
#         newNode = Node(data,self.head)
#         self.head = newNode
#         self.size += 1
#         return True

# # 4- Define print node function to test out the input and output
#    def printNode(self):
#        curr = self.head
#        while curr:
#            print(curr.data)
#            curr = curr.getNextNode()

# myList = LinkedList()
# print("Inserting")
# print(myList.addNode(5))
# print(myList.addNode(15))
# print(myList.addNode(25))
# print("Printing")
# myList.printNode()
# print("Size")
# print(myList.getSize())



# Create node #
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# 2nd Signly Linked List #

# create linkedlist #
# class SLinkedList:
#     def __init__(self):
#         self.headval = None

# # Print the linked list
#     def listprint(self):
#     # start from head value #
#         printval = self.headval
#     # as long as there is value in headval #
#         while printval is not None:
#             print (printval.dataval)
#     # equals printval to nextval so it prints it out
#             printval = printval.nextval

# # Define function that adds Nodes to the beginning #
#     def AtBegining(self,newdata):
#         NewNode = Node(newdata)
#         # Update the new nodes nextval to existing node
#         NewNode.nextval = self.headval
#         self.headval = NewNode

# list = SLinkedList()
# headValueNode = Node("Mon")
# list.headval = headValueNode
# e2 = Node("Tue")
# e3 = Node("Wed")

# list.headval.nextval = e2
# e2.nextval = e3

# list.AtBegining("Sun")

# list.listprint()

# class Node:
#     def __init__(self, data = None, nextNode = None):
#         self.data = data
#         self.nextNode = nextNode

# class LinkedList:
#     def __init__(self):
#         self.headValue = None
    
#     def listprint(self):
#         # headValue = self.headValue
#         while self.headValue is not None:
#             print (self.headValue.data)
#             self.headValue = self.headValue.nextNode    


# list1 = LinkedList()
# list1.headValue = Node("First Node")
# list2 = Node('Second Node')
# list3 = Node("Third Node")
# list1.headValue.nextNode = list2
# list2.nextNode = list3
# list1.listprint()



# Linked List try number 3 #
# class node:
#     def __init__(self, data = None):
#         self.data = data
#         self.nextNode = None

# class MyLinkedList:
#     def __init__(self):
#         self.Linked_List_Nodes = None

#     def printList(self):
#         while self.Linked_List_Nodes is not None:
#             print(self.Linked_List_Nodes.data)
#             self.Linked_List_Nodes = self.Linked_List_Nodes.nextNode

# list1 = MyLinkedList()
# list1.Linked_List_Nodes = node("First Thing")
# list2 = node("Second Things")
# list1.Linked_List_Nodes.nextNode = list2
# list1.printList()



# Doubly Linked List #

# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.next = None
#       self.prev = None

# class doubly_linked_list:

#    def __init__(self):
#       self.head = None

# # Adding data elements		
#    def push(self, NewVal):
#       NewNode = Node(NewVal)
#       NewNode.next = self.head
#       if self.head is not None:
#          self.head.prev = NewNode
#       self.head = NewNode

# # Print the Doubly Linked list		
#    def listprint(self, node):
#       while (node is not None):
#          print(node.data),
#          last = node
#          node = node.next

# dllist = doubly_linked_list()

# dllist.push(12)
# dllist.push(8)
# dllist.push(62)

# dllist.listprint(dllist.head)




