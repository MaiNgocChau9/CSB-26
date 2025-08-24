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

arr = sorted(random.sample(range(100),20))
num = random.choice(arr)
print(arr)
print(num)

start = time.time()
print(linear_search(arr, num))
end = time.time()
print(f"Linear Search: Time Taken={end-start:.6f}s")

start = time.time()
print(binary_search(arr, num))
end = time.time()
print(f"Binary Search: Time Taken={end-start:.6f}s")