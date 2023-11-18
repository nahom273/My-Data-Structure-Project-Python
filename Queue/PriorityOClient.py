
 

from PriorityQ import *
def first(x):
   return x[0]


QU=PriorityQueue(10,first)

for record in [(0, 'Ada'), (1, 'Don'), (2, 'Tim'), (0, 'Joe'), (1, 'Len'), (2, 'Sam'), (0, 'Meg'), (0, 'Eva'), (1, 'Kai')]:
    QU.insert(record)

print(f"After inserting {len(QU)} persons on the QU, it contains:\n{QU}")
print(f'Is QU full? {QU.isFull()}')

print("Removing items from the QU:")
while not QU.isEmpty():
    print(QU.remove(), end=' ')
print()
