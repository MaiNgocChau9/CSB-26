tong = 0
while True:
    a = input("Nhap so: ")
    if a == "":
        break
    try:
        a = int(a)
    except ValueError:
        print("Khong phai la so nguyen. Vui long nhap lai.")
        continue
    tong += a
    
print("Tổng:",tong)