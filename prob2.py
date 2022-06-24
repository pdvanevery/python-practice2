def mult_list(list):
    result = 1
    for x in list:
        result = result * x
    return result


list = [2, 7, 2]

print(mult_list(list))