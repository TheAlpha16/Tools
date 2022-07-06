
def gaussSchidel(eq1, eq2, eq3, ini_sol):
    a11, a12, a13, b01 = eq1[0], eq1[1], eq1[2], eq1[3]
    a21, a22, a23, b02 = eq2[0], eq2[1], eq2[2], eq2[3]
    a31, a32, a33, b03 = eq3[0], eq3[1], eq3[2], eq3[3]
    p, q, r = ini_sol[0], ini_sol[1], ini_sol[2]

    x = (b01 - (a12 * q) - (a13 * r)) / a11
    y = (b02 - (a21 * x) - (a23 * r)) / a22
    z = (b03 - (a31 * x) - (a32 * y)) / a33

    return [x, y, z]


def parse(st1, st2, st3):
    Eq1 = [0, 0, 0, 0]
    Eq2 = [0, 0, 0, 0]
    Eq3 = [0, 0, 0, 0]

    init_set = [st1, st2, st3]
    ret_set = [Eq1, Eq2, Eq3]

    for i in range(3):

        k, l, m, n = map(int, init_set[i].strip().split(' '))

        if k >= l+m:
            ret_set[0] = list(map(int, init_set[i].strip().split(' ')))
        elif l >= k+m:
            ret_set[1] = list(map(int, init_set[i].strip().split(' ')))
        elif m >= k + l:
            ret_set[2] = list(map(int, init_set[i].strip().split(' ')))

        else:

            print("Check Diagonal dominance")
            exit(1)

    return ret_set


if __name__ == '__main__':
    print("-----------------------------------------------------------")
    print("Please enter equation coefficients with spaces in between")
    print("for this equation 2x + 3y - 4z = 5 enter")
    print("2 3 -4 5")
    print("-----------------------------------------------------------")

    try:
        string1 = input("Equation-1: ")
        string2 = input("Equation-2: ")
        string3 = input("Equation-3: ")
        initial_set = input("Enter initial solution set: ")

        no = int(input("Enter no of iterations: "))
        print("-----------------------------------------------------------")

        stet = parse(string1, string2, string3)

        initial_sol = list(map(int, initial_set.strip().split(' ')))
        if len(initial_sol) != 3:
            print("Please Check initial solution set")
            exit(1)

        count = 0
        while count < no:
            soln = gaussSchidel(stet[0], stet[1], stet[2], initial_sol)
            print(f'{count + 1} {soln}')
            initial_sol = soln
            count += 1

    except ValueError:
        print("-----------------------------------------------------------")
        print("Enter valid integer for no. of iterations")

    except UnboundLocalError:
        print("-----------------------------------------------------------")
        print("Follow correct syntax for equations")

    print("-----------------------------------------------------------")

    

