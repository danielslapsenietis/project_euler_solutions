def sum():

    x = list(range(1, 101))
    sum_one, sum_two = 0, 0

    for i in x:
        kapinajums = pow(i, 2)
        sum_one += kapinajums
        sum_two += i
        sum_two_total = sum_two ** 2

    total = sum_two_total - sum_one
    return total

print(sum())