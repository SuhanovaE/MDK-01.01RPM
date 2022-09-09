a = int(input())
space = a - 1
star = 1
for i in range(1, a + 1):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2
