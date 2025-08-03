class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def display_info(self):
        return f"Xe màu {self.color} đã chạy được {self.mileage} km"

car_1 = Car("xanh", 20)
car_2 = Car("đỏ", 30)

print(car_1.display_info())
print(car_2.display_info())