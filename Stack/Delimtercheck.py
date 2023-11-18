from SimpleStackMe import *

stack = Stack(100)

error = 0 

Expr = input("enter expression to be checked")

for pos,letter in enumerate(Expr):
    if letter in "{([":
        if stack.isFull():
            raise Exception("the stack is overflowed")
        else:
            stack.push(letter)
    elif letter in "}])":
        if stack.isEmpty():
            print(f"you have an error pos {pos} and no left matching for {letter}")
            error +=1
        else:
            left = stack.pop()
            if not (left == '(' and letter == ')' or
                      left  == '{' and letter == '}' or
                      left == '['  and letter == ']' ):
                error +=1



if stack.isEmpty and error == 0:
    print("expression is balanced")
elif not stack.isEmpty :
    print("there is problem")
 

    

        
