def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonacci(n - 2) + fibonacci(n - 1))

liste = []

for n in range(1, 50):
    x = fibonacci(n)
    liste.append(x)
    if x >= 3999999:
        break

liste.pop()

divides_by_two = []

for i in liste:
    if i % 2 == 0:
        divides_by_two.append(i)

print(sum(divides_by_two))