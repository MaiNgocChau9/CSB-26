ds = list(map(int, input("Nhập các số: ").split()))
print(sum([num for num in ds if num % 2 == 0]))