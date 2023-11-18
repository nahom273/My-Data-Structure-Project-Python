def identity(x):
    return x

class LinkedList:
    
    class Node:
         
        def __init__(self,data,next=None):
            self.__data = data
            self.__next = next

        def isLast(self) -> bool:
            return self.__next == None
        
        def getData(self):
            return self.__data
        
        def getNext(self):
            return self.__next
    
        def setData(self,newData):
            self.__data =newData

        def setNext(self,newlink):
            if newlink is None or isinstance(newlink,LinkedList.Node):
                self.__next = newlink
            else:
                raise Exception("next node must be node ty")
        def __str_(self):
            return str(self.getData())
        
    def __init__(self):
        self.__head = None

    def insertFront(self,newData):
        newNode = LinkedList.Node(data=newData,next=self.__head)
        self.__head = newNode 
    

    def isEmpty(self):
        return self.__head == None
    

    def insertBack(self,newData):
        CurrentNode= self.__head
        while CurrentNode.getNext() is not None:
            CurrentNode = CurrentNode.getNext()
        newNode = LinkedList.Node(data = newData)
        CurrentNode.setNext(newNode)
    

    def find(self, keygoal,key = identity):
        CurrentNode = self.__head
        while CurrentNode is not None:
            if keygoal == key(CurrentNode.getData()):
                return CurrentNode
            CurrentNode = CurrentNode.getNext()
        return None


    def search(self,keygoal,key= identity):
        FoundNode = self.find(keygoal,key)
        CurrentNode = self.__head
        while CurrentNode is not None:
            if keygoal == key(CurrentNode.getData()):
                return CurrentNode.getData()
            CurrentNode = CurrentNode.getNext()
        return None
    

    def traverse(self,func=print):
        CurrentNode = self.__head
        while CurrentNode is not None:
            func(CurrentNode.getData())
            CurrentNode = CurrentNode.getNext()
    
    def __len__(self):
        count = 0
        CurrentNode = self.__head
        while CurrentNode is not None:
            count +=1
            CurrentNode = CurrentNode.getNext()
        return count
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("lk is empty")
        return self.__head.getData()
        self.__head = self.__head.getNext()

    def __str__(self):
        result ="["
        CurrentNode = self.__head
        while CurrentNode is not None:
            if len(result)> 1:
                result ="-->>"
            result += str(CurrentNode.getData())
            CurrentNode = CurrentNode.getNext()
        result += "]"
        return result


    def delete(self,keygoal,key=identity):
        if self.isEmpty():
            raise("the can not delte it is empty")
        if keygoal == key(self.__head.getData()):
            self.deleteFirst()
        pnode =  self.__head
        while (pnode.getNext() is None and key(pnode.getNext().getData()) != keygoal):
            pnode += pnode.getNext()
        result = pnode.getNext().getData()
        pnode.setNext(pnode.getNext().getNext())
        return result


 
        





             