class Array(object):
    def __init__(self,intialSize):
        self.__a=[None] * intialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems
    
    def get(self,n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
    def set(self,n,value):
        if 0 <= n and n <= self.__nItems:
            self.__a[n]=value
    def insert(self,value):
        self.__a[self.__nItems]=value
        self.__nItems += 1


    def find(self,item):
        for j in range(self.__nItems):
            if self.__a[j]==item:
                return j
        return -1
 # here we can do it the search find + set
 # this will return index
    def search(self,item):
        return self.get(self.find(item))
    
    # the second for it must start
    #from the index where it finds it
    # use the index as the staring for the second loop
    # then rearange every positon one minus
    def delete(self,item):
        for j in range(self.__nItems):
            if self.__a[j]==item:
                self.__nItems-=1
                for k in range(j,self.__nItems):
                    self.__a[k]=self.__a[k+1]
                return True
            return False
    def traverse(self,function=print):
        for j in range(self.__nItems):
            function(self.__a[j])
