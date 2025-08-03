def count(ds, num):
    count = 0
    for i in ds:
        if i == num:
            count += 1
    return count

def tinh_mode(ds):
    ds.sort()
    count_max_num = 0
    for i in ds:
        if count(ds, i) > count_max_num:
            count_max_num = count(ds, i)
            count_max_num = i
    return count_max_num

print(tinh_mode([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5]))