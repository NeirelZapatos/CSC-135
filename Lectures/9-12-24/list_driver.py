from persistant_list import List135

a = List135()
b = a.add(1)
print(b.first())  # this should print 1
c = b.add(2)
d = a.add(3)
e = c.add(4)  # [4, 2, 1]
f = e.rest()  # [2, 1]
e.empty()  # should print false
a.empty()  # should print true
g = b.add(None)  # [None, 1]


def length(xs):
    if xs.empty():
        return 0
    else:
        temp = length(xs.rest())
        return temp + 1


# loop way
def loop_length(xs):
    acc = 0
    while not xs.empty():
        acc = acc + 1
        xs = xs.rest()
    return acc


# tail recursive way
def tail_length(xs, acc):
    if xs.empty():
        return acc
    else:
        return tail_length(xs.rest(), acc + 1)
