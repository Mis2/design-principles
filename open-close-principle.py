## Example of implementation of open-close principle ##
## No change in GraphicalEditor class or Shape class on introduction of new shape ###
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class Rectangle (Shape):
    def draw(self):
        print("4")
class Triangle(Shape):
    def draw(self):
        print("3")
class GraphicalEditor():
    def drawShape(self,s):
        s.draw()

if __name__ == "__main__":
    r = Rectangle()
    t = Triangle()
    g = GraphicalEditor()
    g.drawShape(r)     
    g.drawShape(t)                      