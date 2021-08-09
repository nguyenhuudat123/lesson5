def is_pangram(str_):
    # đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    k = 0
    str_2 = str_.lower()
    for char in range(97, 122+1):
        for item in str_2:
            if ord(item) == char:
                k += 1
        if k == 0:
            return 0
    return 1

print(is_pangram("zxcvbnm,./asdfghjkl;'QWERTtyuiop["))
