import random

def binary_search(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = random.sample(range(100),30)
arr.sort()
print(arr)
num = int(input("So: "))
print(f"Vị trí của {num} trong mảng là: {binary_search(arr, num)}")