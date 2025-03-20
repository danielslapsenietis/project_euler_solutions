def smallest_number():

    x = list(range(1, 2600))
    y = list(range(1, 20))

    for i in x:
        for j in y:
            if i % j == 0:
                print(i)

print(smallest_number())


##################### UNSOLVED #####################
# gave up after 1h 10min solving