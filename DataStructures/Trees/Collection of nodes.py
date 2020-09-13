class Node(object):
    def __init__(self, value= None):
        self.data = value
        self.left = None
        self.right = None 
        
    def set_left(self, node):
        self.left = node 
        
    def set_right(self, node):
        self.right = node
        
    def has_right(self):
        return self.right != None

    def has_left(self):
        return self.left != None
      
        
root = Node('apple')
node1 = Node('orange')
node2 = Node('banana')
print(root.has_left())
print(root.has_right())
root.set_right(node1)
root.set_left(node2)
print(root.has_left())
print(root.has_right())
print(root.data, root.left.data, root.right.data)
