
# Linked List insertion #
class Node:

    def __init__(self, rootData):

        self.left = None
        self.right = None
        self.rootData = rootData

# Define insert function #
    def insert(self, data):
# Compare the new value with the parent node
        # If rootData is true/exist
        if self.rootData:
            
            if data < self.rootData:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.rootData:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.rootData),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()