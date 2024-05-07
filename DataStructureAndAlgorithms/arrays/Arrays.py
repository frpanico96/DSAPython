"""
Arrays
"""
import array
import numpy as np


def traverse_array(arr):
    for i in arr:
        print(i)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


arr = array.array('i', [1, 2, 3, 4])
arr.insert(0, 6)
print(arr)
traverse_array(arr)
print(linear_search(arr, 2))

"""
Numpy Array
"""
np_arr = np.array([], dtype=int)
print(np_arr)

arr.remove(1)
print(arr)

"""
Multi dimensional array
"""
twoDimArray = np.array([[11, 15, 10, 6],
                        [10, 14, 11, 5],
                        [12, 17, 12, 8],
                        [15, 18, 14, 9]
                        ])

print(twoDimArray)
# column axis=1 | row axis=0
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDimArray)
