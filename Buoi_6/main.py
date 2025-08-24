def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

def binary_search(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5]
num = 1
# result = linear_search(arr, num)
# print(f"Vị trí của {num} trong mảng là: {result}")

result = binary_search(arr, num)
print(f"Vị trí của {num} trong mảng là: {result}")