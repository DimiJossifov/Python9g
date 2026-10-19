k = 0
num = int(input("Enter a number: "))

for i in range(1, num):
    if num % i == 0:
        if i % 2 == 1:
            print(i)
            k += 1

print("Imash", k ,"nehcetni delitelq\n")