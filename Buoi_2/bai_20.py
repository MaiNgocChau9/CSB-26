print("Nhập tên học sinh:")
ds = []
while True:
    ten = input()
    if ten == '':
        break
    ds.append(ten)
with open('ten_hocsinh.txt', 'w') as f:
    f.write('\n'.join(ds))