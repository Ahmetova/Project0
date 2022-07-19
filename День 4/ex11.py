d = {}

def update_dictionary(d, key, value):
    if len(d) == 0:
        d[2 * key] = [value]
    else:
        if key in d:
            d[key].append(value)
        elif 2 * key in d:
            d[2 * key].append(value)
        else:
            d[2 * key] = value

#update_dictionary(d, 1, -1)
#print(d)

#update_dictionary(d, 2, -2)
#print(d)

#update_dictionary(d, 1, -3)
#print(d)