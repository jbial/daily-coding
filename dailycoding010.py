from threading import Thread
import time


def func(ms):
    print(f"It's been {ms} milliseconds")


def scheduler(f, n):
    time.sleep(n)
    f()


def main():

    job = Thread(target=scheduler, args=(lambda: func(0.01), 0.01))
    job.start()

    print("Before")
    time.sleep(0.02)
    print("After")


if __name__ == '__main__':
    main()
