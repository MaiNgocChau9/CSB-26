# Bài 10 (Nâng cao): Viết chương trình cho phép người dùng chọn phương pháp tìm kiếm (linear hoặc binary). Chương trình sẽ sinh mảng ngẫu nhiên, sắp xếp nếu cần, và hiển thị vị trí tìm thấy cùng với thời gian chạy.

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

arr = random.sample(range(100),30)
arr.sort()
print("Mảng đã sắp xếp:", arr)
num = int(input("Nhập số cần tìm: "))
method = input("Chọn phương pháp tìm kiếm (linear/binary): ").strip().lower()
if method == "linear":
    start = time.time()
    result = linear_search(arr, num)
    end = time.time()
    print(f"Linear Search: Vị trí của {num} trong mảng là: {result}")
    print(f"Time Taken={end-start:.6f}s")
elif method == "binary":
    start = time.time()
    result = binary_search(arr, num)
    end = time.time()
    print(f"Binary Search: Vị trí của {num} trong mảng là: {result}")
    print(f"Time Taken={end-start:.6f}s")
else:
    print("Phương pháp tìm kiếm không hợp lệ. Vui lòng chọn 'linear' hoặc 'binary'.")