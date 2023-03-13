count = 0
numbers = 0
while True:
    n = int(input())
    if n == 0:
        print(numbers / count)
    else:
        count += 1
        numbers += n