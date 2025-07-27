ds = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
new_ds = [ds[0]]
for i in range(1, len(ds)):
    if ds[i] != ds[i-1] and ds[i] not in new_ds:
        new_ds.append(ds[i])
print(new_ds)