import random
import time

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

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

arr = sorted(random.sample(range(50000),50000))
num = random.choice(arr)

start = time.time()
result = linear_search(arr, num)
end = time.time()
print(f"Linear Search: Time Taken={end-start:.6f}s")

start = time.time()
result = binary_search(arr, num)
end = time.time()
print(f"Binary Search: Time Taken={end-start:.6f}s")
"""
Linear Search: Time Taken=0.001049s
Binary Search: Time Taken=0.000023s
=> Thời gian tìm kiếm nhị phân nhanh hơn rất nhiều so với tìm kiếm tuần tự trong mảng có 50,000 phần tử.
"""