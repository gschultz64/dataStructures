def insert(list):
    # i = 1
    # j = i
    for i in range(1, len(list)):
        j = i
        while i < len(list):
            while (j > 0 and list[j - 1] > list[j]):
                # swap list[j] and list[j - 1]
                x = list[j]
                list[j] = list[j - 1]
                list[j - 1] = x
        i = i + 1

    return list

insert([4, 1, 3, 9, 7])
