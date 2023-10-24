a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
D = b ** 2 - 4 * a * c
if D > 0:
    print('x1:', (-b + D ** 0.5) / (2 * a))
    print('x2:', (-b - D ** 0.5) / (2 * a))
elif D == 0:
    print('x:', -b / (2 * a))
