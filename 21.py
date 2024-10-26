conversion = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
]

def to_roman(n):
    ones = conversion[0][n % 10]
    n //= 10
    tens = conversion[1][n % 10]
    n //= 10
    hundreds = conversion[2][n % 10]
    n //= 10
    return 'M' * n + hundreds + tens + ones

print(to_roman(2348))