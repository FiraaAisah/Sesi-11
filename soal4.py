def count_unique_elements(my_list):
    unique_elements = set(my_list)
    return len(unique_elements)

my_list = [1, 2, 3, 3, 4, 4, 5]
jumlah_unik = count_unique_elements(my_list)
print(jumlah_unik)

