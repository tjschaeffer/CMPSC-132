#LAB 12
#Due Date: 11/22/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class MinHeap:
    ### Copy and paste your code from LAB 9 here
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
    	deleted = self.heap[0]
    	current = 1
    	self.heap[0] = self.heap[len(self.heap)-1]
    	self.heap.pop()
    	moved_value = 1
    	while self.leftChild(current)!= None:
            if self.leftChild(current) < self.heap[0] and self.rightChild(current) > self.leftChild(current):
            	i = self.heap.index(self.leftChild(current))
            	self.swap(0, i)
            	current = current * 2
            elif self.rightChild(current) != None and self.rightChild(current) < self.heap[0] and self.rightChild(current) < self.leftChild(current):
            	i = self.heap.index(self.rightChild(current))
            	self.swap(0, i)
            	current = current * 3
            	moved_value = 2
            else:
            	if self.rightChild(current) != None and self.rightChild(current) < self.leftChild(current):
            		i = self.heap.index(self.rightChild(current))
            		self.swap(0, i)
            		moved_value = 2*moved_value+2
            		current = current*2+1
            	if self.rightChild(current) != None and self.leftChild(current) < self.rightChild(current):
            		i = self.heap.index(self.leftChild(current))
            		self.swap(moved_value, i)
            		moved_value = 2*moved_value+2
            		current = current*2
            	if self.rightChild(current) != None and self.leftChild != None:
            		i = self.heap.index(self.leftChild(current))
            		self.swap(moved_value, i)
            		moved_value = 2*moved_value+2
            		current = current*2
    	return deleted



def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sort_heap = MinHeap()
    # -- YOUR CODE STARTS HERE
    while numList:
    	sort_heap.insert(numList.pop(-1))
    return sort_heap