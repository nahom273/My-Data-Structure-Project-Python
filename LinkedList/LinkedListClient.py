from LinkedList import *

link = LinkedList.Node(data=2)
assert link.isLast() == True
assert link.getData() == 2
assert link.getNext() == None

link2= LinkedList.Node(3,link)
assert link2.isLast() == False
assert link2.getData() == 3 
link2.setData(5)
assert link2.getData() == 5 
assert link2.getNext() == link

link3 = LinkedList.Node(5)
link3.setNext(link2)
assert link3.getNext() == link2



isAssertionRaised = False
try:
    link3.setNext(8)
except Exception:
    isAssertionRaised = True
assert isAssertionRaised == True

linkedList1 = LinkedList()
assert linkedList1.isEmpty() == True
linkedList1.insertFront(33)
assert linkedList1.isEmpty() == False
linkedList1.insertFront(44)
linkedList1.insertBack(56)
linkedList1.insertBack(56)
linkedList1.traverse()

assert linkedList1.deleteFirst() == 44
assert len(linkedList1) == 4