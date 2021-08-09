def min_max(*str):
    min_ = str[0]
    max_ = str[0]
    for i in str:
        if i > max_:
            max_ = i
        if i < min_:
            min_= i
    print(f'min = {min_}, max = {max_}')


min_max(1,2,3,5)

