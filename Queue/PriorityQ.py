def identity(x):
    return x

class PriorityQueue(object):
    def __init__(self,size,priority=identity):
        self.__maxSize = size
        self.__queue = [None] * size
        self.__priority = priority
        self.__nItems = 0
    
    def insert(self,item):
        if self.isFull():
            raise Exception("Q is full")
        j=self.__nItems -1
        while j>=1 and self.__priority(item)>=self.__priority(self.__queue[j]):
            self.__queue[j+1]=self.__queue[j]
            j=j-1
        self.__queue[j+1]=item
        self.__nItems += 1
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("array is empty")
        temp = self.__queue[self.__nItems - 1]
        self.__nItems -= 1
        self.__queue[self.__nItems]=None
        return temp
    

    def isFull(self):
        return self.__nItems == self.__maxSize
    
    def isEmpty(self):
        return self.__nItems == 0
    

    def __len__(self):
        return self.__nItems
    

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if (len(ans))>1:
                ans += ','
            ans += str(self.__queue[i])
        ans += ']'
        return ans




        
        





