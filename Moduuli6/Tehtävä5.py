def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            # lisätään arvo uuteen listaan, jos se on prillinen
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7,8, 1, 3, 5 ]
even_numbers = get_even_numbers(numbers)
print(f'alkuperäiset luvut: {numbers} parilliset luvut: {even_numbers}')