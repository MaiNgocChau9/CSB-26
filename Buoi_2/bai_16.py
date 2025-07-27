def dem_tan_suat(ds):
    ds.sort()
    last_so = 0
    for so in ds:
        if so == last_so:
            last_so = so
            continue
        else:
            print(f"Số {so} xuất hiện {ds.count(so)} lần")
            last_so = so
dem_tan_suat(list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split())))