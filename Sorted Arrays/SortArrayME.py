class SortArrayME(object):

    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

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

    def swap(self,x,y):

        if (0 < x and x < self.__nItems) and (0 < y and y < self.__nItems):
            self.__a[x],self.__a[y]=self.__a[y],self.__a[x]
        return False
    
# self.len # no jus call it by len()   
    def insert(self,item):
            # check if the array is full or not
        if (self.__nItems >= len(self.__a)):
                raise Exception ("Array is full")
            # here it adds it at the last of the item
        self.__a[self.__nItems]=item
        self.__nItems += 1
    

    def find(self,item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                return i
        return -1
    


    def delete(self,item):
        for i in range(self.__nItems):
            if self.__a[i]== item:
                for j in range(i+1,self.__nItems):
                    self.__a[j]=self.__a[j+1]
                return True
        return False


    def bubbleSort(self):
        for outer in range(self.__nItems-1,0,-1):
            for inner in range(outer):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner,inner + 1)

    def selectionSort(self):
        for outer in range(self.__nItems-1): # it will  check from the next positon t
                                         # thas why nitems -1
            mid=outer # set the min first
            for inner in range(outer+1,self.__nItems): # it will start from  next pos
                if self.__a[inner] < self.__a[mid]: #  check condition then 
                       mid=inner  # assign the smallest new value
            
            self.swap(inner,mid) # afer checking all in one travere ie when inner loop finish do swap


    def insertionSort(self):
     # no swap funciton
        # uses while loop
        for outter in range(1,self.__nItems):
            temp=self.__a[outter] # put temporay storage
            inner=outter #inner loop run n times as the number it gets from outtr
        # this for loop works it compares the temp with each left sort arr then, the inner ,inner -1 
            while inner > 0 and temp < self.__a[inner-1]: # inner > 0 to check not to go negative 
               self.__a[inner] = self.__a[inner-1]   # 
               inner -= 1
            self.__a[inner] = temp  
    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])


        



            




            




