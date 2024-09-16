# first - return the first element of a list
# add - returns a new list with added element
# rest - returns list without the first element
# empty - is list empty
# new empty list

class List135:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def add(self, data):
        return List135(data, self)

    def first(self):
        return self.data

    def rest(self):
        return self.next

    def empty(self):
        return self.next is None




