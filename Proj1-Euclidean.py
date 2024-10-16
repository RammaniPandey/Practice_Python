#A user can find out the distance between 2 coordinates
#A user can find find the distance of a coordinate from origin

class point:

    #parametrized constructor
    def __init__ (self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def dist_from_origin(self):
        #return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.euclidean_distance(point(0,0))
    



class line:
    def __init__(self,A,B,C) -> None:
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)
    
    def point_line(line,point):
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            return " lies on the line"
        else:
            return "Does not lies" 
        
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5



l1 = line(1,1,-2)
p1 = point(1,5)
print(l1)
print(p1)
print(l1.shortest_dist(p1))
#print(l1.point_line(p1))
# ob = point(0,0)
# ob2 = point(10,10)
# print("The Euclidean Distance is : ",ob.euclidean_distance(ob2))
# print("The Distance is: ",ob.dist_from_origin())
