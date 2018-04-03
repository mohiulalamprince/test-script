from operator import attrgetter

class A():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

a1 = A(1, 2, 3)

arr = []

arr.append(a1)


c1 = A(5,4,2)
arr.append(c1)

b1 = A(4, 3, 1)
arr.append(b1)


arr = sorted(arr, key=attrgetter('x'), reverse=True)

for item in arr:
    print item.x

