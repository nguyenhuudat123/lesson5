def find_x(a_list, x):
    # trả lại vị trí x trong a_lít, nếu k thì trả lại -1
    return list(filter(lambda i: a_list[i] == x, a_list))