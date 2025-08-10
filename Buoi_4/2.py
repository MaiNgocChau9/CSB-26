class TaiKhoan:
    def __init__(self, ten, sodu):
        self.ten = ten
        self.sodu = sodu
    
    def nap_tien(self, so_tien):
        self.sodu += so_tien
        print(f"Đã nạp {so_tien} vào tài khoản. Số dư hiện tại: {self.sodu}")
    
    def rut_tien(self, so_tien):
        if so_tien > self.sodu:
            print("Số dư không đủ để rút tiền.")
        else:
            self.sodu -= so_tien
            print(f"Đã rút {so_tien} từ tài khoản. Số dư hiện tại: {self.sodu}")
    def lay_so_du(self):
        print(f"Số dư hiện tại của tài khoản {self.ten} là: {self.sodu}")

class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, ten, sodu, lai_suat):
        super().__init__(ten, sodu)
        self.lai_suat = lai_suat
    
    def tinh_lai_suat(self):
        lai = self.sodu * self.lai_suat / 100
        print(f"Lãi suất hiện tại: {self.lai_suat}%. Lãi suất tính được: {lai}.")
        return lai
    

if __name__ == "__main__":
    tk = TaiKhoan("Nguyen Van A", 100000)
    tk.nap_tien(50000)
    tk.rut_tien(30000)

    tktk = TaiKhoanTietKiem("Nguyen Van B", 200000, 0.05)
    tktk.nap_tien(50000)
    tktk.rut_tien(30000)
    tktk.tinh_lai_suat()