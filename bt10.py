#tri fibonaci
def trifibonaci1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n ==3:
        return 2
    return trifibonaci1(n-1) + trifibonaci1(n-2) + trifibonaci1(n-3)

def _trifibonaci2(m):
    i1 =1
    i2 =1
    i3 =2
    if m == 1:
        return i1
    if m == 2:
        return i2
    if m == 3:
        return i3
    j = 4
    sum_ = 0
    while j <= m:
        sum_ = i1 + i2+ i3;
        i1= i2
        i2= i3
        i3= sum_
        j += 1
    return sum_
