def prime_number_in_a_row(n):
    prime_number_list = []
    x = list(range(2, 1000000))

    for i in x:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Only check up to sqrt(i) for efficiency
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_number_list.append(i)
            if len(prime_number_list) == n:
                return prime_number_list[-1]

print(prime_number_in_a_row(10001))

############### SOLVED WITH HELP OF CHATGPT ###############