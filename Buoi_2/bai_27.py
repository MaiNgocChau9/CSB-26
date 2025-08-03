with open('diem.txt', 'r') as f:
    ds = [float(line.strip()) for line in f if line.strip()]
tb = sum(ds) / len(ds)
print(f"Điểm trung bình: {tb}")