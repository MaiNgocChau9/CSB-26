with open('so_nhap.txt', 'r') as f:
    ds = [int(line.strip()) for line in f]
so_le = []
for so in ds:
    if so % 2 != 0:
        so_le.append(so)
with open('so_le.txt', 'w') as f:
    f.write("".join(f"{so}\n" for so in so_le))