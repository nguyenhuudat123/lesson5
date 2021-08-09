import math
def is_prime(n):
    #   kiểm tra xem số tự nhiên n có phải số nguyên tố hay không,
    # nếu có thì trả lại True, nếu không thì trả lại False
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n % 2 == 0:
            return 0
        else:
            for i in range(3, int(math.sqrt(n)), 2):
                if n % i == 0:
                    return 0
                    break
            return 1
print("is_prime") if is_prime(int(input("nhap so tu nhien: "))) else print('isnt _prime')
