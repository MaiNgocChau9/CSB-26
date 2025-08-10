from abc import ABC, abstractmethod

# Lớp Item – đại diện cho từng món hàng
class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


# Lớp Promotion – lớp cha TRỪU TƯỢNG cho các loại khuyến mãi
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Trả về số tiền được giảm (không phải %)."""
        pass


# Lớp con 1 – Khuyến mãi cho đơn hàng số lượng lớn
class BulkOrderPromo(Promotion):
    RATE = 0.10          # giảm 10%
    THRESHOLD = 10       # tổng số lượng từ 10 trở lên

    def discount(self, order):
        total_qty = sum(item.quantity for item in order.item_list)
        return order.total_price() * self.RATE if total_qty >= self.THRESHOLD else 0


# Lớp con 2 – Khuyến mãi cho khách hàng thân thiết
class LoyaltyPromo(Promotion):
    RATE = 0.15          # giảm 15%

    def discount(self, order):
        is_loyal = order.customer_id.startswith("VIP") or getattr(order, "is_loyal_customer", False)
        return order.total_price() * self.RATE if is_loyal else 0


# Lớp Order – đại diện cho một đơn hàng
class Order:
    def __init__(self, customer_id, item_list, promotion=None, is_loyal_customer=False):
        self.customer_id = customer_id
        self.item_list = item_list
        self.promotion = promotion          # LoyaltyPromo, BulkOrderPromo hoặc None
        self.is_loyal_customer = is_loyal_customer

    def total_price(self):
        return sum(item.total_price() for item in self.item_list)

    def total(self):
        subtotal = self.total_price()
        discount = self.promotion.discount(self) if self.promotion else 0
        # Không cho giảm vượt quá tổng tiền
        discount = min(discount, subtotal)
        return subtotal - discount


# ----------------------------
# Chạy thử chương trình (đã điều chỉnh để có 1 đơn đạt ngưỡng "bulk")

# Tạo danh sách món hàng
item1 = Item(2, 100)   # 2 món giá 100 = 200
item2 = Item(1, 200)   # 1 món giá 200 = 200
item3 = Item(8, 50)    # 8 món giá 50 = 400  -> tổng số lượng = 11 (>= 10)
items = [item1, item2, item3]  # Tổng trước giảm: 800

# Đơn hàng 1: Khách VIP → LoyaltyPromo (15%)
order1 = Order("VIP001", items, LoyaltyPromo())

# Đơn hàng 2: Khách thường nhưng số lượng lớn → BulkOrderPromo (10%)
order2 = Order("CUS002", items, BulkOrderPromo())

# Đơn hàng 3: Không khuyến mãi
order3 = Order("CUS003", items)

# In kết quả
print("Đơn hàng VIP:", order1.total(), "VND")               # 800 - 15% = 680
print("Đơn hàng số lượng lớn:", order2.total(), "VND")      # 800 - 10% = 720
print("Đơn hàng không khuyến mãi:", order3.total(), "VND")  # 800