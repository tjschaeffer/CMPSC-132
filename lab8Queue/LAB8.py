#Lab #8
#Due Date: 10/25/2019, 11:59PM
########################################
#
# Name:
# Collaboration Statement:
#
########################################
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
    def __str__(self):
        return "Node({})".format(self.value)
 
    __repr__ = __str__
 
 
class Queue:
    '''
       >>> x=Queue()
       >>> x.isEmpty()
       True
       >>> x.dequeue()
       'Queue is empty'
       >>> x.enqueue(1)
       >>> x.enqueue(2)
       >>> x.enqueue(3)
       >>> x.dequeue()
       1
       >>> x.reverse()
       >>> x
       Head:Node(3)
       Tail:Node(2)
       Queue:3 2
   '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
 
    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'
 
    __repr__=__str__
 
 
    def enqueue(self, x):
        if self.tail is None:
            self.head =Node(x)
            self.tail =self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
 
 
 
# Function to remove first element and return the element from the queue
    def dequeue(self):
        if self.isEmpty() is True:
            return 'Queue is empty'
 
        if self.head is None:
            return None
        else:
            temp= self.head.value
            self.head = self.head.next
            return temp
 
 
# Function to return the size of the queue
    def __len__(self):
 
        temp=self.head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count
 
 
# Function to check if the queue is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        return False
 
    def reverse(self):
        current = self.head
        previous = None
        oldHead = self.head
        while current is not None:
            follow = current.next
            current.next = previous
            previous = current
            current = follow
        self.head = previous
        self.tail = oldHead