import random
doan = random.randint(1, 10)
dap_an = 0
while dap_an != doan:
    dap_an = int(input("Đoán số từ 1 đến 10: "))
    if dap_an < doan:
        print("Số bạn đoán quá nhỏ.")
    elif dap_an > doan:
        print("Số bạn đoán quá lớn.")
    else:
        print("Chúc mừng bạn đã đoán đúng!")
        break