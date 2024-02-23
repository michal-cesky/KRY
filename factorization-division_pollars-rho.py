import math
import random

def factorization_by_division(n):
    ar = []

    while n % 2 == 0:
        ar.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while (n % i == 0):
            ar.append(i)
            n = n / i

    if n > 2:
        ar.append(n)
    return ar

def Pollars_rho_algorithm(n):

    x0 = (random.randint(0, 2))
    xi = x0

    d=1
    while (d == 1):
        x0 = (pow(x0, 2, n) + n) % n

        xi = (pow(xi, 2, n) + n) % n
        xi = (pow(xi, 2, n) + n) % n

        d = math.gcd(abs(x0 - xi), n)

        if (d == n):
            return Pollars_rho_algorithm(n)

    return d


if __name__ == '__main__':

    n = 4918641

    cv1 = factorization_by_division(n)
    print("Rozklad čísla", n, "je:", cv1)

    cv2 = Pollars_rho_algorithm(n)
    print("Netriviální dělitel je:", Pollars_rho_algorithm(n))




