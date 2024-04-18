class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return (self.size*"🍪")


    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity or capacity <0:
            raise ValueError()
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size <= self.capacity:
            self._size = size
        else:
            raise ValueError()
        if self.size < 0:
            raise ValueError

def main():
    jar = Jar(12,0)
    jar.deposit(int(input("How many Cookies you want to add? ")))
    jar.withdraw(int(input("How many Cookies you need? ")))
    print(jar)

if __name__=="__main__":
    main()