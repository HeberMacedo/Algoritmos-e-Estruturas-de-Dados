from math import gcd

N = int(input())

for _ in range(N):
    N1, _, D1, operator, N2, _, D2 = input().split()

    N1 = int(N1)
    D1 = int(D1)
    N2 = int(N2)
    D2 = int(D2)

    if operator == '+':
        numerator = N1 * D2 + N2 * D1
        denominator = D1 * D2
    elif operator == '-':
        numerator = N1 * D2 - N2 * D1
        denominator = D1 * D2
    elif operator == '*':
        numerator = N1 * N2
        denominator = D1 * D2
    else:
        numerator = N1 * D2
        denominator = D1 * N2

    originalnumerador = numerador
    originaldenominador = denomindor

    divisor = gcd(
        abs(numerador), 
        abs(denominador)
    )

    numerador //= divisor
    denominador //= divisor

    if denominador < 0:
        numerador *= -1
        denominador *= -1

    print(
        f"{originalnumerador}/{originaldenominador} = {numerador}/{denominador}"
    )