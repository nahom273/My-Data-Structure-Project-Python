from SimpleStackMe import *
max=10
Sto = Stack(max)

for x in ['sdf','asd','asdf','asdfsd']:
    Sto.push(x)

len(Sto)
print(Sto)
print("is full",Sto.isFull())

while not Sto.isEmpty():
    print(Sto.pop(),end='')# end to print it in one line
print()
















