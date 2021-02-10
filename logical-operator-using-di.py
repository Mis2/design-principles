 
class Operator():
    def result(self):
        pass
class Binary(Operator):
    def __init__(self,a,b):
        super().__init__()
        self.x = a
        self.y = b
    def result(self):
        pass
class Unary(Operator):
    def __init__(self,a):
        self.x = a
    def result(self):
        pass
class Not(Unary):
    def __init__(self,a):
        super().__init__(a)
    def result(self):
        print (not(self.a))
class And(Binary):
    def __init__(self,a,b):
        super().__init__(a,b)
    def result(self):
        print (self.x and self.y)
class Or(Binary):
    def __init__(self,a,b):
        super().__init__(a,b)
    def result(self):
        print (self.x or self.y)
class Gate():
    g = Operator()
    def __init__(self,a):
        self.g = a
    def outcome(self):
        self.g.result() 
if __name__== "__main__":
    obj = And(1,0)
    gate = Gate(obj)
    gate.outcome()
