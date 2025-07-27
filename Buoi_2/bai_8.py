def loc_chan(ds):
    return [num for num in ds if num % 2 == 0]
print(loc_chan([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))