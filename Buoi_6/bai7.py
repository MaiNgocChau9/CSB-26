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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Nhập điểm cần kiểm tra: "))
result = binary_search(arr, num)
if result != -1:
    print(f"Học sinh đạt điểm {num} tại vị trí: {result}")
else:
    print(f"Không có học sinh đạt điểm {num}")
