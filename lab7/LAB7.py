#Lab #7
#Due Date: 10/11/2019, 11:59PM 
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
                        
                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.remDuplicates()
        >>> x.pop()
        8.76
        >>> x
        Head:Node(1)
        Tail:Node(5)
        List:1 3 5
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
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count


    def add(self, value):
        # --- Your code starts here
        active = self.head
        last = None
                
        temp = Node(value)
        if self.head == None:
            self.head = temp
            self.tail = temp
        elif self.head.value >= temp.value:
            temp.next = self.head
            self.head = temp
        elif self.tail.value <= temp.value:
            temp.next = self.tail
            self.tail = temp
        else:
            while active.next.value is not None and active.next.value < temp.value:
                active = active.next
            temp.next = active.next
            active.next = temp 

    def pop(self):
        # --- Your code starts here
        if self.head is None:
            return 
        if self.head == self.tail: # if only one value since its in order
            return self.head
        
        last = self.head
        while last.next != self.tail:
            last = last.next
        value = self.tail.value
        self.tail = last
        last.next = None
        return(value)


    def remDuplicates(self):
        # --- Your code starts here
        temp = self.head 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.value == temp.next.value: 
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else: 
                temp = temp.next
        





