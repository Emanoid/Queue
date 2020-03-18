import array as array
import ctypes as c
import string as string

import string as string
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None        
    
    def get_head(self):
        return self._head

    #To make the given node the head
    def insert_head(self, node):
        node.change_link(self._head)
        self._head = node

    #To insert the given node into head avoiding repeated data
    def insert_head_2(self, node):
        if self.search(self._head, node.get_data()) == True:
            print("Error: Node already exists!")
        else:
            node.change_link(self._head)
            self._head = node
        
    #To get the last node in the Linked List
    #   To help the insert_tail function
    def get_last(self):
        Done = False
        node = self._head
        while Done is not True:
            if node.get_link() == self._tail:
                Done = True
                return node
            else:
                node = node.get_link()

    #To make the given node the tail of the LinkedList       
    def insert_tail(self, node):
        node.change_link(self._tail)
        self.get_last().change_link(node)
    
    #To remove node at head of the LinkedList
    def remove_head(self):
        self._head = self._head.get_link()
    
    #To remove node at tail of LinkedList
    def remove_tail(self):
        self.removetailhelper(self._head)

    #To help the remove_tail function
    def removetailhelper(self, node):
        if node != None:
            if node.get_link().get_link() == None:
                node.change_link(None)
            else:
                self.removetailhelper(node.get_link()) 

    #To Print out all the nodes in the LinkedList
    def printl(self, node):
        if (node != None):
            print(node.get_data())
            self.printl(node.get_link())

    #To mutate the data in the head node
    def change_head(self,data):
        self._head.change_data(data)

    #To mutate the data in the tail node
    def change_tail(self,data):
        self.get_last().change_data(data)

    #To compute if a node-data is in the LinkedList
    def search(self,node,key):
        if (node != None and node.get_data() == key):
            return True
        elif(node != None and node.get_link() != None):
            return self.search(node.get_link(),key)
        else:
            return False

    #To remove a node from the LinkedList
    def remove(self, data):
        elem = []
        elem = self.removehelper(self._head, elem)
        elem.remove(data)
        elem.reverse()
        self._head = None
        for i in elem:
            self.insert_head(Node(i,None))

    #To help the remove function
    def removehelper(self,node,elem):
        if (node != None):
            elem.append(node.get_data())
            self.removehelper(node.get_link(),elem)
        return elem
        
##################################################################################
class Node:
    #Node: data Node
    def __init__(self,data,link):
        self._data = data
        self._link = link
    
    #To get the data in a node
    def get_data(self):
        return self._data
    
    #To mutate the data in a node
    def change_data(self, data):
        self._data = data
    
    #To get node that is linked to this node
    def get_link(self):
        return self._link
    
    #To mutate the node that is linked to this node
    def change_link(self, link):
        self._link = link
############################################################################################
class Queue_Linked_List:

    def __init__(self):
        LIST = LinkedList()
        self._items = LIST
    
    def isEmpty(self):
        return self._items.get_head() == None

    def push(self, data):
        node = Node(data,None)
        self._items.insert_head(node)

    def pop(self):
        item = self._items.get_last().get_data()
        self._items.remove(item)
        return item

    def top(self):
        item = self._items.get_last()
        return item.get_data()

    def _len_(self):
        i = 0
        node = self._items.get_head()
        while node != None:
            i += 1
            node = node.get_link()
        return i

    def print(self):
        return self._items.printl(self._items.get_head())

'''
#Tests
MyQueue = Queue_Linked_List()
print(MyQueue.isEmpty())
for i in range(15):
    MyQueue.push(i+1)
print(MyQueue.isEmpty())
MyQueue.push(16)
print(MyQueue.pop())
print(MyQueue.top())
print(MyQueue._len_())
MyQueue.print()
'''