# Change this function

def f(x, y):
    num = y**2 - x**2
    den = y**2 + x**2
    fun_value = num / den

    return fun_value


def main(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + (h/2), y + (k1/2))
    k3 = h * f(x + (h/2), y + (k2/2))
    k4 = h * f(x + h, y + k3)

    result = y + (k1 + (2*k2) + (2*k3) + k4)/6
    return result


if __name__ == '__main__':
    print("-----------------------------------------------------------")

    try:
        x = float(input('Enter previous x value: ').strip())
        y = float(input('Enter previous y value: ').strip())
        h = float(input('Enter step value: ').strip())
        n = int(input('Enter the number of steps: ').strip())

        print("-----------------------------------------------------------")


        count = 0
        while count < n:
            final = main(x, y, h)
            print(f"{count + 1}{final}")
            x += h
            y = final
            count += 1

    except ValueError:
        print("-----------------------------------------------------------")
        print("Please enter valid values")
        exit(1)