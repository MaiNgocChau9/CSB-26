from bai_2 import tinh_mean
from bai_3 import tinh_median
from bai_4 import tinh_mode

ds = []
with open("data.txt", "r") as f:
    ds = [int(num) for num in f.read().split()]
print("Mean:", tinh_mean(ds))
print("Median:", tinh_median(ds))
print("Mode:", tinh_mode(ds))