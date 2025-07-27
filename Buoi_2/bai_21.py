def tong_chan(ds):
    return sum(so for so in ds if so % 2 == 0)

ds = list(map(int, input("Nhập danh sách số: ").split()))
print("Tổng các số chẵn:", tong_chan(ds))
