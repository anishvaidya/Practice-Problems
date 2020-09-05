#import sys
#data = sys.stdin.readlines()
#print ("Counted", len(data), "lines.")
#%%
print ('Building a stack')
class Stack:
    def __init__(self):
        self._data_ = list()
    def push(self, item):
        self._data_.append(item)
    def pop(self):
        element = self._data_[-1]
        print ("Popping element:", element)
        del self._data_[-1]
    def show(self):
        for element in reversed(self._data_):
            print ("\n", element)
            
#%%
print ("Building a linked list")

# creating a node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, new_next):
        self.next = new_next
  
# creating linked list    
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            return
        tail = self.head
        while (tail.next):
            tail = tail.getNext()
        tail.setNext(new_node)
        
    def size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.getNext()
        return size
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print (current_node.getData())
            current_node = current_node.getNext()
            
    def reverseList(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        
    def countDuplicate(self):
        current_node = self.head
        items = set()
        duplicate_count = 0
        while current_node:
            item = current_node.data
            if (item not in items):
                items.add(item)
            else:
                duplicate_count += 1
            current_node = current_node.next
        print (duplicate_count)
        
    def sortList(self):
        sorted = False
        while not sorted:
            sorted = True
            current_node = self.head
            next_node = current_node.next
            while (next_node != None):
                if (current_node.data > next_node.data):
                    sorted = False
                    current_node.data, next_node.data = next_node.data, current_node.data
                current_node = next_node        
                next_node = next_node.next
        print ("Sorted linked list is:")
        self.traverse()
        
#    def mergeSort(self):
#        sorted = False
#        mid = self.size() / 2
#        
#        while not sorted:
#            
        
    
                
                    
#%%
ll = LinkedList()
ll.insertAtStart(2)
ll.insertAtEnd(3)
ll.insertAtStart(4)
ll.insertAtEnd(3)
ll.insertAtEnd(2)
ll.traverse()
print("---------")
ll.sortList()
#ll.traverse()
#ll.countDuplicate()
#%%