"""
Array Practice
"""
from array import *

arr = array('i', [1, 2, 3, 4, 5])
# Traverse array
print('####')
for i in arr:
    print(i)
print('####')
for i in range(len(arr)):
    print(arr[i])
print('####')
arr.append(4)
print(arr)
print('####')
arr.insert(len(arr), 6)
print(arr)
print('####')
arr.extend(array('i', [7, 8, 9, 10]))
print(arr)
print('####')
tmpList = [11, 12, 13, 14]
arr.fromlist(tmpList)
print(arr)
print('####')
arr.remove(3)
print(arr)
print('####')
arr.pop()
print(arr)
print('####')
print(arr.index(6))
print('####')
arr.reverse()
print(arr)
print('####')
print(arr.buffer_info())
print('####')
print(arr.count(8))
print('####')
arrList = arr.tolist()
print(arrList)
print('####')
# charArr = array('b', ['a', 'b', 'c'])
# charArr.fromstring('def')
# print(charArr)
print('####')
print(arr[1:4])
print('####')


