import random
import time
def linear_search(arr, num):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    return count

arr_100 = random.sample(range(1000), 100)
arr_10000 = random.sample(range(10000), 10000)
num_100 = random.choice(arr_100)
num_10000 = random.choice(arr_10000)        

# print(arr_100)
# print(num_100)
start = time.time()
result_100 = linear_search(arr_100, num_100)
end = time.time()
print(f"Time Taken={end-start:.6f}s")

# print(arr_10000)
# print(num_10000)
start = time.time()
result_10000 = linear_search(arr_10000, num_10000)
end = time.time()
print(f"Time Taken={end-start:.6f}s")

"""
Time Taken=0.000012s
Time Taken=0.000524s
=> Thời gian tìm kiếm trong mảng 10,000 phần tử lâu hơn mảng 100 phần tử rất nhiều.
"""