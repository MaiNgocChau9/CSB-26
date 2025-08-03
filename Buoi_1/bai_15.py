diem_trung_binh = float(input("Nhập điểm trung bình: "))
if diem_trung_binh >= 8 and diem_trung_binh <= 10:
    print("Bạn đạt loại Giỏi")
elif diem_trung_binh >= 6.5:
    print("Bạn đạt loại Khá")
elif diem_trung_binh >= 5:
    print("Bạn đạt loại Trung bình")
else:
    print("Bạn đạt loại Yếu")