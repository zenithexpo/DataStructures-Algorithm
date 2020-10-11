#!/usr/bin/env python
# coding: utf-8

# # Linked List Practice
# 
# Implement a linked list class. You have to define a few functions that perform the desirbale action. Your `LinkedList` class should be able to:
# 
# + Append data to the tail of the list and prepend to the head
# + Search the linked list for a value and return the node
# + Remove a node
# + Pop, which means to return the first node's value and delete the node from the list
# + Insert data at some position in the list
# + Return the size (length) of the linked list

# In[1]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# In[2]:


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# #### Task 1. Write definition of `prepend()` function and test its functionality

# In[6]:


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
        return 
    tmp_node = Node(value)
    tmp_node.next = self.head
    self.head = tmp_node
    return 


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


# <div id="spoiler_1" style="display:none">
# Here is an example of a Makefile you could create for this exercise:
# ```
# cmd1:
#         @echo "$@"
# 
# cmd2:
#         @echo "$@"
# 
# all: cmd1 cmd2
# ```
# 
# Note that after `cmd1` and `cmd2`, and before `@echo`, should be a tab. The `@` at the start of these lines prevents `make` from automatically printing the lines, while `"$@"` is the variable for a string containing the target name, in this case either `cmd1` or `cmd2`. To double-check that `make` is actually showing the command name from within the command itself, try to `echo` something else from within one of them, such as `Hello World!`, and check the results.
# </div>
# <button title="Click to show/hide content" type="button" onclick="if(document.getElementById('spoiler_1') .style.display=='none') {document.getElementById('spoiler_1') .style.display=''}else{document.getElementById('spoiler_1') .style.display='none'}">Show Solution</button>
# 
# ```{toggle} Click the button o your right to reveal the solution!
# 
# def prepend(self, value):
#     """ Prepend a node to the beginning of the list """
# 
#     if self.head is None:
#         self.head = Node(value)
#         return
# 
#     new_head = Node(value)
#     new_head.next = self.head
#     self.head = new_head
# ```

# In[7]:


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


# #### Task 2. Write definition of `append()` function and test its functionality

# In[8]:


def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here
   
    if self.head is None:
        self.head = Node(value)        
        return
    curr = self.head
    while curr.next:
        curr= curr.next
    curr.next = Node(value)
    
    

LinkedList.append = append


# In[9]:


# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"


# In[10]:


# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"


# #### Task 3. Write definition of `search()` function and test its functionality

# In[11]:


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head is None:
        return None
    curr = self.head
    while curr:
        if curr.value == value:
            return curr
        curr= curr.next

LinkedList.search = search


# In[12]:


# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


# #### Task 4. Write definition of `remove()` function and test its functionality

# In[15]:


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head is None:
        return None
    if self.head.value == value:
        self.head = self.head.next
        return
    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next
   
            

LinkedList.remove = remove


# In[16]:


# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"


# #### Task 5. Write definition of `pop()` function and test its functionality

# In[23]:


def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head is None:
        return None
    old_head = self.head
    self.head = self.head.next
    return old_head.value

LinkedList.pop = pop


# In[24]:


# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# #### Task 6. Write definition of `insert()` function and test its functionality

# In[ ]:


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here    
    counter = 0
    if pos == 1:
        node = Node(value)
        node.next = self.head
        self.head = node
    cur = self.head
    while counter != pos-1 and curr.next:
        curr= curr.next
        

LinkedList.insert = insert


# In[ ]:


# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"


# #### Task 7. Write definition of `size()` function and test its functionality

# In[25]:


def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    if self.head is None:
        return None
    size = 0
    curr = self.head
    while curr:
        size+=1
        curr = curr.next
    return size

LinkedList.size = size


# In[26]:


# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"


# <span class="graffiti-highlight graffiti-id_1vt6pt0-id_q7rr1km"><i></i><button>Hide Solution</button></span>

# In[ ]:


# Solution

#----------------------------------------------------#
def prepend(self, value):
    """ Prepend a node to the beginning of the list """

    if self.head is None:
        self.head = Node(value)
        return

    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
#----------------------------------------------------#
def append(self, value):
    """ Append a node to the end of the list """
    # Here I'm not keeping track of the tail. It's possible to store the tail
    # as well as the head, which makes appending like this an O(1) operation.
    # Otherwise, it's an O(N) operation as you have to iterate through the
    # entire list to add a new tail.

    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)
#----------------------------------------------------#
def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None

    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found in the list.")

#----------------------------------------------------#
def remove(self, value):
    """ Delete the first node with the desired data. """
    if self.head is None:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next

    raise ValueError("Value not found in the list.")

#----------------------------------------------------#
def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    node = self.head
    self.head = self.head.next

    return node.value
#----------------------------------------------------#
def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
    # If the list is empty 
    if self.head is None:
        self.head = Node(value)
        return
        
    if pos == 0:
        self.prepend(value)
        return

    index = 0
    node = self.head
    while node.next and index <= pos:
        if (pos - 1) == index:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return

        index += 1
        node = node.next
    else:
        self.append(value)
        
#----------------------------------------------------#

def size(self):
    """ Return the size or length of the linked list. """
    size = 0
    node = self.head
    while node:
        size += 1
        node = node.next

    return size
#----------------------------------------------------#

def to_list(self):
    out = []
    node = self.head
    while node:
        out.append(node.value)
        node = node.next
    return out

