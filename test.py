class Point:   #to je trida
    
    def __init__(self, x=0, y=0): # self = jeste nevim jak se bude jmenovat tenhle objekt
        self.__x = x   #hodnota s "__" udela privatni/skryty vlastnost, to znamena ze tohle nejde pouzit
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

j = Point(3, 5) #j = je objekt

print(j.get_x(), j.get_y()) # pouzijeme to abysme mohli pouzit privatni vlastnosti

print(j.x, j.y)

w = Point()  # kdyz nemame definovano souradnice, vzdycky bude default (v tom def __init__)

print(w.x, w.y) 

w.x = 10

print(w.x, w.y)

w.x, w.y = 10, 15

print(w.x, w.y)

