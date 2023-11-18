def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    for i in range(11):
        print(f"the factorial of {i} is factorial of {factorial(i)}")

