# this is iterative approach using loops 

def triangular(nth):
    number = 0
    for i in range(1,nth+1):
        number += i
    return number

# here doesnot use any loops

def traingular(nth):
    if nth == 1 :
        return 1
    return nth + triangular(nth - 1)


# more clarified one

def show_traingular(nth):
    print(f" printing the  num {nth} ")
    if nth == 1:
        print("the is first case so is 1")
        return 1
    value=nth + traingular(nth -1)
    print(f"the {nth} have {value} numbers")
    return value


if __name__ == "__main__":
    for i in range(1,11):
        print(f"{i}th is num {show_traingular(i)}")



