'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
    
class Node(object):
    def __init__(self, value= None):
        self.data = value
        self.left = None
        self.right = None 
        
    def set_left(self, node):
        self.left = node 
        
    def set_right(self, node):
        self.right = node
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right        
        
    def has_right(self):
        return self.right != None

    def has_left(self):
        return self.left != None
        
class Tree(object):
    def __init__(self, node):
        self.root = node 
        
    def get_root(self):
        return self.root
    
        
def preOrder(node):
    if(node):
        print(node.data, end=" ")
        preOrder(node.left)
        preOrder(node.right)
        
def inOrder(node):
    if(node):
        inOrder(node.left)
        print(node.data, end=" ")
        inOrder(node.right)
        
def postOrder(node):
    if(node):
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end=" ")
        
root = Node('apple')
root.set_left(Node('banana'))
root.set_right(Node('cherry'))
root.get_left().set_left(Node('dates'))

preOrder(root)
print('\n')
inOrder(root)
print('\n')
postOrder(root)



