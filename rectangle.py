class Rectangle:

    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b   

    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def get_obsah(self):
        return self.__a * self.__b
    
    def get_obvod(self):
        return 2 * (self.__a * self.__b)
    
r = Rectangle(10, 20)
print("Obsah:", r.get_obsah())
print("Obvod:", r.get_obvod())