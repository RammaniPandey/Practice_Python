class fraction:


    #Parameterized Constructor
    def __init__(self,x,y):
    #    x = int(input("Enter Numerator: "))
    #    y = int(input("Enter Denominator: "))
       self.num=x
       self.den=y

    def __str__(self): # magic method --> superpower --> ye btayega ki karna kya hai class ko exactly
        return '{}/{}'.format(self.num,self.den)
    
# for addition
    def __add__(self,other):
        new_num = self.num * other.den + other.num *self.den
        new_den = self.den * other.den

        return '{}/{}'.format(new_num,new_den)
    
# for Subs     
    def __sub__(self,other):
        new_num = self.num * other.den - other.num *self.den
        new_den = self.den * other.den

        return '{}/{}'.format(new_num,new_den)
    
#for multiplication   
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num,new_den)
    
#for division
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return '{}/{}'.format(new_num,new_den)

#for decimal    
    def convert_to_decimal(self):
        return self.num/self.den




if __name__ == "__main__":
   fr1 = fraction(3,4)
   fr2 = fraction(5,4)



   print(fr1 + fr2)
   print(fr1 - fr2)
   print(fr1 * fr2)
   print(fr1 / fr2)

    