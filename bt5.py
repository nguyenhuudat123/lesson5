def count_upper_lower(str_):
    # trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
    upper_ = 0
    lower_ = 0
    for item in str_:
        if 'a' <= item <= 'z':
            lower_ += 1
        if 'A' <= item <= 'Z':
            upper_ += 1
    print('so chu viet hoa: ', upper_)
    print("so chu viet thuwong: ", lower_)


count_upper_lower('asdifnIHJKDNJfjadsf345')
