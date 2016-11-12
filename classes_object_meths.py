class Bio(object):
    def __init__(self, last, first, mi, age):
        self.last= last
        self.first = first
        self.mi = mi
        self.age = age

miss_piggy = Bio("Piggy", "Miss", "Peepants", 4)

print(miss_piggy.__dict__)

del miss_piggy.age

print(miss_piggy.__dict__)
