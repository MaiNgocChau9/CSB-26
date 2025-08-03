import datetime
nam_sinh = int(input("Nhập năm sinh: "))
tuoi = datetime.datetime.now().year - nam_sinh
print(f"Bạn {tuoi} tuổi.")