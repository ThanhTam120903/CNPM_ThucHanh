n = int(input("Nhập số nguyên n: "))

# Hình 1: Hình chữ nhật
print("Hình 1:")
for i in range(n):
    print('*' * n)

# Hình 2: Hình tam giác ngược
print("Hình 2:")
for i in range(n):
    print('*' * (n - i))

# Hình 3: Hình tam giác cân
print("Hình 3:")
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# Hình 4: Hình tam giác ngược cân
print("Hình 4:")
for i in range(n):
    print(' ' * i + '*' * (2 * (n - i) - 1))
