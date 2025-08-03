def dem_le(ds):
    return sum(1 for num in ds if num % 2 != 0)
print(dem_le([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))