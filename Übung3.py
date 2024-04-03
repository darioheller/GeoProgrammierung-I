import math

class Figur:
    def __init__(self):
        self.name = "Figur" 
    
    def umfang(self):
        return 0 
    
    def __str__(self):
        return self.name
    
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__("Dreieck")
        self.a = a
        self.b = b
        self.c = c

    def umfang(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"{self.name} mit folgenden Seitenlänegn: A={self.a}, B={self.b}, C={self.c}"

class Rechteck(Figur):
    def __init__(self, p1, p2):
        super().__init__("Rechteck")
        self.p1 = p1
        self.p2 = p2

    def umfang(self):
        return 2 * (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))

    def __str__(self):
        return f"{self.name} über die beiden Koordinaten {self.p1} und {self.p2}"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.m = mittelpunkt
        self.r = radius
        
    def umfang(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return f"{self.name} mit Mittelpunkt={self.m} und Radius={self.r}"


class Polygon(Figur):
    def __init__(self, *punkte):
        super().__init__("Polygon")
        self.punkte = punkte

#Folgende Lösung von ChatGPT --> Gibt es eine bessere Lösung?

    def umfang(self):
        perimeter = 0
        for i in range(len(self.punkte) - 1):
            x1, y1 = self.punkte[i].x, self.punkte[i].y
            x2, y2 = self.punkte[i + 1].x, self.punkte[i + 1].y
            perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        x1, y1 = self.punkte[-1].x, self.punkte[-1].y
        x2, y2 = self.punkte[0].x, self.punkte[0].y
        perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return perimeter

    def __str__(self):
        punkte_str = " ".join([str(point) for point in self.punkte])
        return f"{self.name} {punkte_str}"