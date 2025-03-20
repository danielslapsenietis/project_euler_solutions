list = []

def division():

    x = 600851475143
    y = range(1, x)

    for i in y:
        if x % i == 0 and i != 1 and i <= x:
            x = x / i
            list.append(i)
            for i in y:
                if x % i == 0 and i != 1 and i <= x:
                    x = x / i
                    list.append(i)
                    for i in y:
                        if x % i == 0 and i != 1 and i <= x:
                            x = x / i
                            list.append(i)
                            for i in y:
                                if x % i == 0 and i != 1 and i <= x:
                                    x = x / i
                                    list.append(i)
                                    return x, i

division()
print(f"""List of prime factors looks like this: {list}
Largest prime factor is: {max(list)}""")