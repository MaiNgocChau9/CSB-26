with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    file1 = [int(num) for num in f1.read().split()]
    file2 = [int(num) for num in f2.read().split()]
merged = file1 + file2
with open("merged.txt", "w") as f:
    f.write("".join(f"{num} " for num in merged))