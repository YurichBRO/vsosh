def fast_pow(a, b, m):
    if b == 0:
        return 1
    if b & 1:
        return a * (fast_pow(a, b-1, m)) % m
    half_pow = fast_pow(a, b >> 1, m)
    return half_pow * half_pow % m

print(fast_pow(123, 65537, 9871))