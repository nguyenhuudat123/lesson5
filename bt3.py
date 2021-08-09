
def is_perfect(n):
    # kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko,
    sum = 0
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, int(n/2)+1):
            if n % i == 0:
                sum += i
    if sum == n:
        return 1
    else:
        return 0


if is_perfect(6):
    print('hh')
else:
    print("khong hh")