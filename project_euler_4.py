def largest_palindrome():

    x = list(range(100, 1000))
    y = list(range(100, 1000))

    palindromes = []

    for i in x:
        for j in y:
            number = i * j
            str_number = str(number)
            if str_number == str_number[::-1]:
                palindromes.append(number)

    return max(palindromes)

print(largest_palindrome())