ds = list(map(int, input("Nhập danh sách số: ").split()))
print("Các số âm:", [x for x in ds if x < 0])
