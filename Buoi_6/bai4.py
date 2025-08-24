def linear_search(arr, num):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    return count

arr = [2, 5, 7, 9, 11, 7, 3, 7, 8, 7]
num = 7
result = linear_search(arr, num)
print(f"Số lần xuất hiện của {num} trong mảng là: {result}")
