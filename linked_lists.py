# Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value) :
        """Creates the new node"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def append(self, value):
        """Adds node to the end"""
        new_node  = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

    def pop(self):
        """Removes the node from the end and returns the value of the node"""
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
            self.head = None

        return temp


    def prepend(self, value):
        """Adds node to the beginning"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True


    def pop_first(self):
        """Pops an element from the beginning"""
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if  self.length == 0:
            self.tail = None
            
        return temp
    
    def get(self, index):
        """Retrieves an element from the given index"""
        if index < 0 or index > self.length-1:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp



    def insert(self, index, value):
        """Insert node to the index"""
        pass

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

