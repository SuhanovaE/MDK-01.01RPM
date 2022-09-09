n = int(input())
iq = int(input())
print(0)
i = 1
s = iq
while i < n:
    a = s / i
    iq = int(input())
    if iq > a:
        print('>')
    elif iq < a:
        print('<')
    else:
        print(0)
    i += 1
    s += iq
