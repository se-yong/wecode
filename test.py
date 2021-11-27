def get_even():
    even_num = []
    for i in range(1, 51):
        if i % 2 == 0:
            even_num.append(i)
    return even_num

print(get_even())
