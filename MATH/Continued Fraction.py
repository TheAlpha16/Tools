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

    return final_lis


def parse(string):
    lis = list(map(int, string.split(', ')))
    return lis


def nice(lis):
    lis.reverse()
    n = len(lis)
    x = 1
    b = lis[0]
    for i in range(n - 1):
        a = lis[i+1]
        x += a*b
        b, x = x, b

    return b, x


def convergents(numerator, denominator):
    lis = fractions(numerator, denominator)

    final_tuples = []
    for i in range(1, len(lis) + 1):
        final_tuples.append(nice(lis[:i]))

    return final_tuples


if __name__ == "__main__":
    print("-----------------------------------")
    try:
        p = int(input("Enter numerator  :  "))
        q = int(input("Enter denominator:  "))
        frats = fractions(p, q)

        print(f"Continued fractions: {frats}")
        print(f"Convergents: {convergents(p, q)}")
        print("-----------------------------------")

    except ValueError:
        print()
        print("Enter integer values!!!")
        exit(1)

    except ZeroDivisionError:
        print()
        print("Cannot generate continued fractions for these values")
        exit(1)
