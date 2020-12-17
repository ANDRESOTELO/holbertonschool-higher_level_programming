#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma, temp = 0, 0
    unique = []
    for x in range(len(my_list)):
        temp = my_list[x]
        if temp not in unique:
            unique.append(temp)
    for y in range(len(unique)):
        suma = suma + unique[y]
    return suma
