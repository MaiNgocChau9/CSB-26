# Lớp Item – Đại diện cho từng món hàng
class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


# Lớp Promotion – Lớp cha cho các loại khuyến mãi
class Promotion:
    def discount(self, order):
        return 0  # Mặc định không giảm giá


# Lớp con 1 – Khuyến mãi cho đơn hàng nhiều sản phẩm
class BulkOrderPromo(Promotion):
    def discount(self, order):
        if len(order.item_list) >= 3:
            return order.total_price() * 0.10  # Giảm 10%
        return 0


# Lớp con 2 – Khuyến mãi cho khách hàng thân thiết
class LoyaltyPromo(Promotion):
    def discount(self, order):
        if order.customer_id.startswith("VIP"):
            return order.total_price() * 0.15  # Giảm 15%
        return 0


# Lớp Order – Đại diện cho một đơn hàng
class Order:
    def __init__(self, customer_id, item_list, promotion=None):
        self.customer_id = customer_id
        self.item_list = item_list
        self.promotion = promotion  # Có thể là LoyaltyPromo, BulkOrderPromo hoặc None

    def total_price(self):
        return sum(item.total_price() for item in self.item_list)

    def total(self):
        discount = self.promotion.discount(self) if self.promotion else 0
        return self.total_price() - discount


# ----------------------------
# Chạy thử chương trình

# Tạo danh sách món hàng
item1 = Item(2, 100)   # 2 món giá 100 = 200
item2 = Item(1, 200)   # 1 món giá 200 = 200
item3 = Item(3, 50)    # 3 món giá 50 = 150
items = [item1, item2, item3]  # Tổng trước giảm: 550

# Đơn hàng 1: Khách VIP → áp dụng LoyaltyPromo
order1 = Order("VIP001", items, LoyaltyPromo())

# Đơn hàng 2: Khách thường → áp dụng BulkOrderPromo (vì có >= 3 món)
order2 = Order("CUS002", items, BulkOrderPromo())

# Đơn hàng 3: Không khuyến mãi
order3 = Order("CUS003", items)

# In kết quả
print("Đơn hàng VIP:", order1.total(), "VND")          # Giảm 15%
print("Đơn hàng nhiều sản phẩm:", order2.total(), "VND")  # Giảm 10%
print("Đơn hàng không khuyến mãi:", order3.total(), "VND")  # Không giảm