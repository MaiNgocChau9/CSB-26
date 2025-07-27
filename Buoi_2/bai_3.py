def tinh_median(ds):
    ds.sort()
    n = len(ds)
    mid = n // 2
    if n % 2 == 0:
        return (ds[mid - 1] + ds[mid]) / 2
    else:
        return ds[mid]
    
print(tinh_median([1, 2, 3, 4, 5]))