def identity(x):
    return x

class PriorityQ(object):
    def __init__(self,max,priority=identity):
        self.__max = max
        self.__nItems = 0
        self.__priority = priority
        self.__queue = [None] * max


    def __len__(self):
        return self.__nItems
    
    def isFull(self):
        return self.__nItems == self.__max
    
    def isEmpty(self):
        return self.__nItems == 0
    
    

    def insert(self,item):
        if self.isFull():
            raise Exception("the queue is full")
        j= self.__nItems - 1
        while j >= 0 and self.__priority(item) > self.__priority(self.__queue[j -1]):
            temp = self.__queue[j-1]
            self.__queue[j-1] = item
            self.__queue[j]= temp
        self.__nItems += 1
        j= j-1
        return True
    
    def remove(self):
        if self.isEmpty():
            raise Exception("empty")
        temp = self.__queue[self.__nItems -1] 
        self.__queue[self.__nItems] = None
        self.__nItems -= 1
        return temp
    
    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans)>1:
                ans += ','
            ans += str(self.__queue[i])
        ans += "]"
        return ans 
    
        






    