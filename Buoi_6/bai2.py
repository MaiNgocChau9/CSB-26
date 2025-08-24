def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr = ["An", "Bình", "Chi", "Dung"]
num = "Chi"
result = linear_search(arr, num)
print(f"Tìm thấy tại vị trí: {result}")