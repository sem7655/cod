def triangle(a, b, c):
    p = (a + b + c) / 2
    l = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return l
