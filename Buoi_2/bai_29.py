ds1 = list(map(float, input("Nhập điểm lớp 1: ").split()))
ds2 = list(map(float, input("Nhập điểm lớp 2: ").split()))
ds_gop = ds1 + ds2
with open('diem_gop.txt', 'w') as f:
    f.write('\n'.join(map(str, ds_gop)))
