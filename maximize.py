def f(x):
    return 80 * x - 30 * x ** 2 - 0.25 * x ** 4  # Функція максимуму


def maximize(f, a, b, epsilon):
    iterations = 0
    while (b - a) / 2 > epsilon:
        xm = (a + b) / 2
        L = b - a
        x1 = a + L / 4
        x2 = b - L / 4
        if f(x1) > f(xm):
            b = xm
            xm = x1
        else:
            if f(x2) > f(xm):
                a = xm
                xm = x2
            else:
                a = x1
                b = x2
        print(f"Iteration - {iterations + 1}")
        print(f"a = {a}, b = {b}\n")
        iterations += 1

    maximum = (a + b) / 2
    return maximum, iterations


a = 1
b = 2
epsilon = 0.001  # Точність

maximum, iterations = maximize(f, a, b, epsilon)
print(f"\nMaximum: {maximum}")
print(f"Iterations needed: {iterations}\n")
res = input("Press eny key to exit ...")