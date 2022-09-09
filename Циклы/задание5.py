password1 = input()
password2 = input()
a = 0
while a == 0:
    if len(password1) < 8:
        print("Короткий!")
        password1 = input()
        password2 = input()
    elif "123" in password1:
        print("Простой!")
        password1 = input()
        password2 = input()
    elif password1 != password2:
        print("Различаются.")
        password1 = input()
        password2 = input()
    else:
        print("OK")
        a += 2
