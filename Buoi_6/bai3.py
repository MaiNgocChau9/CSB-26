import random

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr = random.sample(range(100),15)
print(arr)
num = int(input("Nhập số cần tìm: "))
result = linear_search(arr, num)
print(f"Vị trí của {num} trong mảng là: {result}")