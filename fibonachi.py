num = int(input("Enter  a number: "))

a, b = 1, 1

for _ in range(num):
    if a > num:
        break
    a, b = b, a + b
    if a + b <= num and b <= num:
        print(a)
