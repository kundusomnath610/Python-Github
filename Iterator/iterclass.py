class iterclass:
    def __init__(self, limit):
        self.count = 0
        self.limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self += 1
            return self.count
        else:
            raise StopIteration
c1 = count(5)
print(c1.__iter__())
print(c1.__iter__())
print(c1.__iter__())