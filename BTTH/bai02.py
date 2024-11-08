n = int(input("Nhập số lượng phần tử n: "))
arr = []

# Nhập dãy số
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i}: "))
    arr.append(num)

# a) Tìm số dương lớn nhất và số âm bé nhất
max_pos = None
min_neg = None
for num in arr:
    if num > 0:
        if max_pos is None or num > max_pos:
            max_pos = num
    elif num < 0:
        if min_neg is None or num < min_neg:
            min_neg = num

print(f"Số dương lớn nhất: {max_pos if max_pos is not None else '*'}")
print(f"Số âm bé nhất: {min_neg if min_neg is not None else '*'}")

# b) Hiển thị tần số xuất hiện của từng phần tử
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Tần số xuất hiện của từng phần tử:")
for num, freq in frequency.items():
    print(f"{num} xuất hiện {freq} lần")

# c) Hiển thị các phần tử xuất hiện k lần
k = int(input("Nhập số lần xuất hiện k: "))
print(f"Các phần tử xuất hiện {k} lần:")
for num, freq in frequency.items():
    if freq == k:
        print(num)

# d) Sắp xếp danh sách giảm dần
arr.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:")
print(arr)
