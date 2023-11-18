from ArrayForMergeSort import *
class Mergesort:
    def __init__(self,unordered):
        self.__array = unordered
        n=len(unordered)
        self.__workingarray = Array(n)
        for i in range(n):
            self.__workingarray.insert(None)
        self.mergesort(0,n)
    

    def mergesort(self,lo,hi):
        if lo + 1 >= hi:
            return
        mid = (lo + hi)//2

        self.mergesort(lo,mid)
        self.mergesort(mid,hi)
        self.merge(lo,mid,hi)

    def merge(self,lo,mid,hi):
        idxlo = lo
        idxhi = mid
      #  hi = hi
        n = 0 
        
        while  idxlo < mid and idxhi < hi:
            itemlo = self.__array.get(idxlo)
            itemhi = self.__array.get(idxhi)
            
            if  itemlo <= itemhi:
                self.__workingarray.set(n,itemlo)
                idxlo+=1
            else :
                self.__workingarray.set(n,itemhi)
                idxhi+=1
            n +=1

        while idxlo < mid:
            itemlo = self.__array.get(idxlo)
            self.__workingarray.set(n,itemlo)
            idxlo += 1
            n+=1

        while n > 0 :
            n-=1
            self.__array.set(lo + n,self.__workingarray.get(n))








        

if __name__ == "__main__":
    items = [12,34,4,33,6,9,0,2]
    Array1 = Array(len(items))
    for i in items:    # rember to iterate through list  #dont use range ...just iterate using name of the list
        Array1.insert(i)
    
    Array1.traverse()

    Mergesort(Array1)



    Array1.traverse()


        






