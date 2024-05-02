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

"""
Space Complexity O(n)
"""


def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)


print(sum(3))

"""
O(1) space complexity
The stack always hold one element in memory
"""


def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i + 1)
    return total


def pair_sum(a, b):
    return a + b


print(pair_sum_sequence(4))

"""
In this case the time complexity
will be O(a + b)
"""


def print_ab_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


print_ab_items(1, 3)

"""
Time complexity will be
O(a*b)
"""
def print_axb_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

print_axb_items(1, 4)