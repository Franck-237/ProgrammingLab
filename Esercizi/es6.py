print("Give a number and stop when insert 0")

sum = 0

x = int(input("Give a numer: "))

while x!=0:
    sum = sum+x
    x = int(input())
    
print(sum)