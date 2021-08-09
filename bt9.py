def count_odd(n):
    #   đếm, trả về só lẻ
    if n == 0:
        return 0
    if n % 2 == 1:
        return count_odd(n // 10) + 1
    else:
        return count_odd(n // 10)
print(count_odd(33234))