

class Jar:
    def __init__(self, capacity = 12, cookies = 0):

        self.capacity = capacity
        self.cookies = cookies


    def __str__(self):
        return f"{self.cookies * "🍪"}"


    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("Cookies exceed jar capacity")


    def withdraw(self, n):
        if not self.cookies - n <= 0:
            self.cookies -= n
        else:
            raise ValueError("No more cookies left")


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be greater than zero")
        self._capacity = capacity





def main():

    jar = Jar()
    jar.deposit(12)

    
    print(jar)




if __name__ == "__main__":
    main()
