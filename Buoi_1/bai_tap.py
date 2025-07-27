n = int(input("Nhập số nguyên dương N: "))
print("# Các số lẻ từ 1 - n: ")
for i in range(1, n+1, 2):
    print(i)
print("# Các ước của N: ", end="")
uoc = []
for i in range(1, n+1):
    if n%i ==0:
        uoc.append(i)
print(uoc)
if len(uoc) == 2:
    print("# N là số nguyên tố")
else:
    print("# N không phải là số nguyên tố")
