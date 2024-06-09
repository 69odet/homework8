my_list = [47, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] >= 0 and i < len(my_list):
    if my_list[i] == 0:
        i += 1
        continue
    else:
        print(my_list[i])
        i += 1
