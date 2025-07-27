with open('so_nhap.txt', 'w') as f:
    while True:
        so = input("Nhập số (hoặc 'x' để kết thúc): ")
        if so == 'x':
            break
        else:
            f.write(so + '\n')