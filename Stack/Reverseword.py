from SimpleStackMe import *

sk=Stack(10)
word = input('Enter the word to reverser')

for letters in word:
    sk.push(letters)

reverse=''

while not sk.isEmpty():
    reverse +=  sk.pop()

print(reverse)
print(len(sk))


    






