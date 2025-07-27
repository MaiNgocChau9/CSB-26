numbers = [2, 4, 6, 8]
write = "".join(f"{str(num)} " for num in numbers)
with open("data.txt", "w") as f:
    f.write(write.strip())