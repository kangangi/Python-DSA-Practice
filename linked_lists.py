# Constructors
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
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp

    def set_value(self,index, value):
        """Set the value for a given index"""

        temp = self.get(index)
        if temp:
            temp.value = value
            return True       
        return False 


    def insert(self, index, value):
        """Insert node to the index"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        return True
    

    def remove(self, index):
        if index < 0 or index >=  self.length:
            return None
        
        if index == 0:
            return self.pop_first(index)
        
        if index == self.length-1:
            return self.pop(index)

        temp = self.get(index)
        pre = self.get(index-1)
        pre.next = temp.next
        temp.next = None
        self.length -= 1 
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


 
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

'''Codiing Challenges'''

'''

LL: Find Middle Node
Implement the find_middle_node method for the LinkedList class.

The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.

If the linked list has an even number of nodes, return the first node of the second half of the list.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node


    def find_middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        return slow


'''
LL: Has Loop
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False
'''

LL: Find Kth Node From End
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the linked list has fewer than k items, the program should return None.

'''

def find_kth_from_end(lst, k):
        
    slow = lst.head
    fast = lst.head
 
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
        
    while fast:

        slow = slow.next
        fast = fast.next
        
    return slow

'''
LL: Reverse Between
You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Input

The method reverse_between takes two integer inputs m and n.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



Output

The method should modify the linked list in-place by reversing the nodes from index m to index n.

If the linked list is empty or has only one node, the method should return None.



Example

Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .



Constraints

The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).


'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def reverse_between(self, m, n):
        dummy = Node(0)
        dummy.next = self.head

        # reach node at position left
        left_prev, cur = dummy, self.head
        for _ in range(m):
            left_prev, cur = cur, cur.next

        # reverse from left to right
        prev = None
        for _ in range(n-m+1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        # updating the pointers
        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next
