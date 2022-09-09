price = float(input())
summa = 0
while price >= 0:
    if price > 500:
        price = price - (price * 0.07)
    summa = summa + price
    price = float(input())
print(summa)

