ds = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
x = int(input("Nhập số cần kiểm tra: "))
if x in ds:
    print(f"Số {x} có trong danh sách.")
else:
    print(f"Số {x} không có trong danh sách.")