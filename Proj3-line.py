
#A user can create and view 2D coordinates

class line:
    def __init__(self,A,B,C) -> None:
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)



ob = line(2,3,4)
print("The Line Equation is:",ob)
