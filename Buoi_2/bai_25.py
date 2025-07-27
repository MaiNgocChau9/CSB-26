ds = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
if ds == ds[::-1]:
    print("Danh sách đối xứng.")
else:
    print("Danh sách không đối xứng.")