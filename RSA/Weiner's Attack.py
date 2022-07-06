from sympy import *


def fractions(a, b):
    final_lis = []
    q = a//b
    x = a - b * q

    while x != 1:
        q = a // b
        final_lis.append(q)

        x = a - b * q
        a = b
        b = x

    final_lis.append(a)
    final_lis.insert(0, 0)

    return final_lis


def parse(string):
    lis = list(map(int, string.split(', ')))
    lis.insert(0, 0)
    return lis


def nice(lis):
    lis.reverse()
    n = len(lis)
    x = 1
    b = lis[0]
    for i in range(n - 1):
        a = lis[i+1]
        x += a*b
        p = b
        b = x
        x = p

    return b, x


def convergent(numerator, denominator):
    lis = fractions(numerator, denominator)
    final_tuples = []
    for i in range(1, len(lis) + 1):
        final_tuples.append(nice(lis[:i]))

    return final_tuples


def solve2(a, b, c):
    x = Symbol('x')
    p = solve(a*(x**2) + b*x + c, x)
    return p


def main(n, e):
    req_list = convergent(n, e)
    for i in range(1, len(req_list)):
        k, d = req_list[i]

        tot = (e*d - 1)//k
        b = n - tot + 1
        tup = solve2(1, -b, n)
        if len(tup) == 1:
            p = tup[0]
            q = tup[0]
        elif len(tup) == 2:
            p, q = tup

        if p*q == n:
            print("Attack Successful")
            return 'p = {}, q = {}, d = {}'.format(p, q, d)
        else:
            pass

    return "Attack Unsuccessful"


if __name__ == '__main__':
    nn = int(input("Enter n: "))
    ee = int(input("Enter e: "))

    fine = main(nn, ee)
    print(fine)