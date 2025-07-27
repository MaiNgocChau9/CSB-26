ds = list(map(int, input("Nhập danh sách số: ").split()))
print("Tổng:", sum(so for so in ds if so > (sum(ds) / len(ds))))
