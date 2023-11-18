class OrderedArray(object):
    def __init__(self,initialSize):
        self.__a = [None] * initialSize
        self.__nItems= 0
    
    def get(self,n):
        if 0 <= n and n <= self.__nItems:
            return self.__a[n]
        raise IndexError("index " + str(n)+ "out of range ")
        
    def __len__(self):
        return self.__nItems
    def __str__(self):
            ans = "["
            for i in range(self.__nItems):
                if len(ans) > 1:
                    ans += ", "
                ans += str(self.__a[i])
            ans += "]"
            return ans
    

    def find(self,item):
        lo = 0
        hi = self.__nItems - 1

        while(lo <= hi):
            mid= (lo+hi)//2
            if self.__a[mid]==item:
                return mid
            elif self.__a[mid] < item:
                lo=mid+1
            else:
                hi=mid-1
        return lo
        
    def search(self,item):
        return self.get(self.find(item))
    


    def traverse(self,function=print):
        print("dfasd")
        for i in range(self.__nItems):
            function(self.__a[i])

    def insert(self,item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array over flow")
        index=self.find(item)

        # we used this -1 because inorder to find
        # if it already ordered it will put at the end
        # but if not will move bigger items direction to move the
        # right place

        for j in range(self.__nItems,index,-1):
            self.__a[j] = self.__a[j-1]
        
        self.__a[index]=item
        self.__nItems += 1 

    def delete(self,item):
        # use find() to find the index
        j=self.find(item)
        self.__nItems -= 1
        if j<self.__nItems and self.__a[j]==item:
            for x in range(j,self.__nItems):
                self.__a[x]=self.__a[x+1]
                return True
        return False
        


        


                

    

        
    
    

