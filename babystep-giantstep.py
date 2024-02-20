import math


def algorithm(c, z, m):
    n = m - 1
    h = math.ceil(math.sqrt(n))

    bs = {pow(c, i, m): i for i in range(h)}

    x = h * (m - 2)
    gs = pow(c, x, m)

    for i in range(h):
        y = (z * pow(gs, i, m)) % m
        if y in bs:
            return i * h + bs[y]
    return "Výsledek nebyl nalezen"


if __name__ == '__main__':
    c = int(5)
    z = int(21)
    m = int(107)

    resault = algorithm(c, z, m)
    print(f"The result is: {resault}")