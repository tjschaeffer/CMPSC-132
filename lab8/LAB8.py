#Lab #8
#Due Date: 10/25/2019, 11:59PM
########################################
# 
# Name: 
# Collaboration Statement:
#
########################################
 
class Node:
    # Initialization
    def __init__(self, value):
        self.value = value
        self.next = None
 
     # String representaion
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
   # Initialization
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
 
    # String representaion
    def __str__(self):
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.value))
            temp=temp.next
        new =' '.join(output)
        if not new:
          return 'Queue is empty'
        else:
          return f'Head:{self.head}\nTail:{self.tail}\nQueue:{new}'

 
    __repr__=__str__

    # Checking if Queue is empty
    def isEmpty(self):
        if self.head is None:
            return True
        return False
 
    # Adding value to queue
    def enqueue(self, x):
        if self.tail is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
 
 
 
    # Removing head value of queue
    def dequeue(self):
        if self.isEmpty() is True:
            return (print('Queue is empty'))
 
        if self.head is None:
            return 

        else:
            temp = self.head.value
            self.head = self.head.next
            return temp
 
 
    # Returning size of queue
    def __len__(self):
 
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # Reversing the queue
    def reverse(self):
        current = self.head
        last = None
        prevHead = self.head
        while current is not None:
            follow = current.next
            current.next = last
            last = current
            current = follow
        self.head = last
        self.tail = prevHead