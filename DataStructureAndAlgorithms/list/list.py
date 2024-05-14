"""
Python Lists

Elements of list don't have to be of the same type
"""
import random

ex_list = ["string", 2, 0, False, [10, 2]]
print(ex_list)

# Tells if the element exist in the list
print(2 in ex_list)
print(4 in ex_list)

# -1 access last element, -2 the second last and so on
print(ex_list[-1])

# List traversing

# elements are readonly with this kind of loop
for i in ex_list:
    print(i)

for i in range(len(ex_list)):
    print(ex_list[i])

# Update/Insert list
int_list = [1, 2, 3, 4, 5, 6, 7]
print(int_list)

int_list[2] = 14
print(int_list)

int_list.insert(0, 11)
int_list.insert(4, 9)
print(int_list)

new_list = [32, 31, 30, 29, 28]
int_list.extend(new_list)
print(int_list)

int_list.append(3)
print(int_list)

# Slice/Delete from list

print(int_list[1:4])
int_list.pop(2)
print(int_list)

del int_list[1:5]
print(int_list)

int_list.remove(32)

# Search element
target = 50
if target in int_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")


def linear_serch(p_list, p_target):
    for j, value in enumerate(p_list):
        if value == p_target:
            return j
        return -1


print(linear_serch(int_list, 500))

#List operations/functions

# list concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
d = a * 3
print(d)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a) / len(a))


def average_input():
    inputs = []
    while (True):
        inp = input("Enter a number: ")
        if inp == "done":
            break
        inputs.append(float(inp))

    if len(inputs) > 0:
        return sum(inputs) / len(inputs)
    else:
        return 0


# print(average_input())

# Strings and list

a = "spam-spam-spam"
b = a.split("-")
print(b)
print("-".join(b))

# list comprehension
prev_list = [1, 2, 3]
new2_list = [i * 2 for i in prev_list]
print(new2_list)

language = "python"
new3_list = [letter for letter in language]
print(new3_list)

# Conditional List Comprehension
prev_list = [-1, 10, -20, 2, -98, 60, 45, 20]
new_list = [number ** 2 for number in prev_list if number > 0]
print(new_list)


def get_number(number):
    return number ** 2 if number < 0 else 0


new_list = [get_number(number) for number in prev_list]
print(new_list)


fruit_list1 = ["Apple", "Berry", "Cherry", "Papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"

sum = 0

for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == "Guava":
        sum += 1
    if ls[1] == "Kiwi":
        sum += 20

print(sum)
