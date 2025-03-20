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

#laižam for loop no 1 - 600,851,475,143 (x), skatāmies, kurš ir pirmais skaitlis, kas dalās ar 600,851,475,143 (i)
#dabūjam pirmo skaitli, kas dalās ar 600851475143 (i = 71)
#pievienojam i (71) listei, no kuras beigās izvilksim max() --> tād būs uzdevuma atbilde
#Tagad mums vajag izdalīt 600,851,475,143 (x) ar 71 (i)
#Iegūstam 8,462,696,833 (jaunais x)
#Tagad vajag veco x (600,851,475,143) aizstāt ar jauno x (8,462,696,833)
#VĒLREIZ laižam for loop, tagad jau ar jauno, updated x no 1 - 8,462,696,833