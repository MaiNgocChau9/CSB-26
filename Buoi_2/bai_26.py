print("Nhập điểm học sinh:")
ds = []
while True:
    diem = input()
    if diem == '':
        break
    else:
        ds.append(diem)
with open('diem.txt', 'w') as f:
    f.write('\n'.join(ds))