num = int(input("Enter a number: "))
a = 0
b = 1
c = 0

for b in range (num):
    
    a = b
    b = a + b
    
    print(b)

