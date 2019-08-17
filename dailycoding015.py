import random
import matplotlib.pyplot as plt


def pick(stream):

    elem = None
    for i, n in enumerate(stream):
        if i == 0:
            elem = n
        elif random.randint(1, i + 1) == 1 + i:
            elem = n
    return elem


def plot_hist(data, bins):
    plt.title("Distribution of selected elements")
    plt.ylabel("Frequency")
    plt.xlabel("Numbers")
    plt.xlim(bins[0], bins[-1])
    plt.hist(data, bins)
    plt.show()


def main():

    stream = [i + 1 for i in range(20)]
    plot_hist([pick(stream) for _ in range(10000)], stream + [21])


if __name__ == '__main__':
    main()
