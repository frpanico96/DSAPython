"""
O(1) constant time complexity
"""


def multiply_numbers(num):
    return num * num


print(multiply_numbers(2))


"""
O(n) linear time complexity
"""

def print_items(n):
    for i in range(n):
        print(i)

print_items(3)

"""
Drop constants
Even if the number of operations are 2n
The order will always be O(n)
"""

def print_2nitems(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_2nitems(3)


"""
O(nˆ2) square time complexity
Non-dominant terms (O(n)) can be dropped
"""

def print_n2items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_n2items(3)