n = int(input())
maxx = n
count = 1
while n != 0: 
    n = int(input())
    if n == maxx: 
        count += 1
    elif n > maxx: 
        maxx = n 
        count = 1
print(count) 