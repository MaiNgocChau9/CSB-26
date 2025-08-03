ds = list(map(int, input("Nhập danh sách số: ").split()))
x = int(input("X: "))
try:
	print("Vị trí:", ds.index(x))
except ValueError:
	print("Vị trí:", -1)