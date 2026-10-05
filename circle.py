class Circle:

    def __init__(self, pi=3.14, r=0):
        self.__pi = pi
        self.__r = r

    def get_pi(self):
        return self.__pi

    def get_r(self):
        return self.__r

    def obsah(self):
        return self.__pi * self.__r ** 2
    
    def obvod(self):
        return 2 * self.__pi * self.__r


c = Circle(3.14, 20)
print("Obsah:", c.obsah())
print("Obvod:", c.obvod())