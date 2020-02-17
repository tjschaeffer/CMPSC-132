#Lab #9
#Due Date: 11/08/2019, 11:59PM
########################################
#                                      
# Name: 
# Collaboration Statement:      
#  
########################################



class MinHeap:
    '''
        >>> h = MinHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h.heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.parent(2)
        2
        >>> h.leftChild(1)
        5
        >>> h.rightChild(1)
        11
        >>> h.parent(8)
        10
        >>> h.leftChild(6)
        >>> h.rightChild(9)
        >>> h.deleteMin
        2
        >>> h.heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
    '''

    # -- YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR!
    def __init__(self):
        self.heap=[]
        
      

    def __str__(self):
    	return f'{self.heap}'

    __repr__=__str__


    def parent(self,index):
        if index <= 1 or index > len(self.heap):
        	return None
        return self.heap[index//2-1]

    def leftChild(self,index):
        if index < 1 or 2*index > len(self.heap):
        	return None
        return self.heap[2*index-1]

    def rightChild(self,index):
        if index < 1 or 2*index + 1 > len(self.heap):
        	return None
        return self.heap[2*index]

    def __len__(self):
        return(len(self.heap))

    def swap(self, index1, index2):
    	self.heap[index1-1], self.heap[index2-1]= self.heap[index2-1], self.heap[index1-1]
 
    def insert(self,x):
        index = len(self.heap)
        self.heap.append(x)
        current = len(self.heap)
        while current>1 and self.parent(current) > self.heap[current-1]:
        	parent_of_x = current//2
        	self.swap(current, parent_of_x)
        	current = parent_of_x
            
    @property
    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            out=self.heap[0]
            self.heap=[]
            return out
        current = self.heap.pop(0)
        last = self.heap.pop()
        self.heap.insert(0, last)
        heap_index = 1
        while self.leftChild(heap_index)!= None and self.rightChild(heap_index)!= None:
            if self.rightChild(heap_index) > self.leftChild(heap_index):
                left = 2*heap_index
                self.swap(left, heap_index)
                heap_index = heap_index + 1
            elif self.leftChild(heap_index) > self.rightChild(heap_index):
                right = 2*heap_index + 1
                self.swap(right, heap_index)
                heap_index = heap_index + 1
            else:
                return current





