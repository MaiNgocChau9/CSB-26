def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr = [2, 5, 7, 9, 11]
num = 7
result = linear_search(arr, num)
print(f"Vị trí của {num} trong mảng là: {result}")
