class QUEUE(object):

    def __init__(self,max):
        self.__maxsize = max
        self.__queue = [None] * max
        self.__nItems=0
        self.__Front=1 # this abt first element, if set 0, prob. is when we want to insert first element then rear will
        #be incremted and then front will be still 0 and rear one will be one 
        self.__Rear=0

    def equeue(self,item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__Rear += 1 # do this at the top,not bottom because rear points to the last elemnt not the next empty position to be inserted
        self.__queue[self.__Rear] = item
        if self.__Rear  == self.__maxsize:
            self.__Rear = 0 
        self.__nItems += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        temp=self.__queue[self.__Front]
        self.__queue[self.__Front] = None
        self.__Front += 1
        if self.__Front == self.__maxsize:
            self.__Front=0
        self.__nItems -=1
        return temp
    

    def peek(self):
        if self.isEmpty():
            return False
        return self.__queue[self.__Front]
    

    def isEmpty(self):
        return  self.__nItems == 0 
    
    def isFull(self):
        return self.__nItems == self.__maxsize
    

    def __len__(self):
        return self.__nItems
    
   
    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans)>1:
                ans += ','
            j = i + self.__Front
            if j >= self.__maxsize:
                j -= self.__maxsize
            ans += str(self.__queue[j])
        ans += "]"
        return ans



    





    

        

  

