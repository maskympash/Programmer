n = int(input("Введіть номер послідовності, що хочете обчислити:"))
x = float(input("x = "))

a = x # a - поточний член нашої послідовності
for k in range(1,n+1):
    # a = - (x ** 2) / ((2*k) * (2*k+1)) * a
    a *= - (x ** 2) / ((2 * k) * (2 * k + 1))


print(a)