# num = int(input("Enter a number: "))
# a = 0
# b = 1
# c = 0

# for b in range (num):
    
#     a = b
#     b = a + b
    
#     print(b)

prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(7):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo