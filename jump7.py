for a in range(1,101):
    if a % 7 == 0 or a % 10 == 7 or a // 7 == 10:
        continue
    else:
        print(a)

