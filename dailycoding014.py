import random


def monte_carlo(iters):

    area_square, area_circle = 0, 0
    new_pi, old_pi = 3, 0
    epsilon = 1e-7

    while abs(new_pi - old_pi) >= epsilon:
        for _ in range(iters):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                area_circle += 1
            area_square += 1
        old_pi = new_pi
        new_pi = 4 * area_circle / area_square
    return new_pi


def main():

    pi = monte_carlo(10000)
    print(f"Approximation of pi: {pi:.3f}")


if __name__ == '__main__':
    main()
