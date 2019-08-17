class Log:

    def __init__(self):
        self.length = 0
        self.log = {}

    def record(self, order_id):
        self.log[self.length] = order_id
        self.length += 1

    def get_last(self, i):
        if 0 < i <= self.length:
            return self.log[self.length - i]
        else:
            return -1


def main():
    log = Log()
    for i in range(100):
        log.record(str(i) + '_12345')
    for i in range(1, 11):
        print(log.get_last(i))


if __name__ == '__main__':
    main()
