# def greet(name):
#     print(f"Good Day {name}")
# name = input("Enter name : ")
# greet(name)

def factorial(n):
    if(n==1) : return 1
    return n * factorial(n-1)

print(factorial(5))
