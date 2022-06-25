def pascal(n):
    for x in range(1, n+1):
        y = 1
        for i in range(1, x+1):
            print(y, end='')
            y = int(y*(x-i)/i)
        print('')

print(pascal(6))
