# assert
a = 1
b = 1

# Trueになる条件とエラー文を記載する
assert a + b == 2, "a + b is equal to 2!"


def power(base, exp):
    return base ** exp
    # return base * exp


assert power(3, 2) == 9, "3の2乗は9だよ"

