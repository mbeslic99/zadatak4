import math
lista_stranica=[(1,2,3),(3,4,5),(3,4,4)]
class Trokut(object):
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
        if (self.__a<0 and self.b__<0 and self.__c<0):
            print("Nije trokut")
        else if(((self.__a+self.__b)<self.__c) and ((self.__a+self.__c)<self.__b) and((self.__b+self.__c)<self.__a)):
            print ("Nije trokut")
        else:
            list_stranica.append(self.__a,self.__b,self.__c)
        
    def a(self):
        return self.__a
    def seta(self,value):
        self.__a=a
    def b(self):
        return self.__b
    def setb(self,value):
        self.__b=b
    def c(self):
        return self.__c
    def setc(self):
        self.__c=c
    
    def __str__(self):
        return ("trokut %s°,%s,%s")%(self.__a,self.__b,self.__c)
    
    def __repr(self):
        return("Trokut(%fm,%fm,%fm)")%(self.__a,self.__b,self.__c)
    def opseg(self):
        return self.__a+self.__b+self.__c
    def povrsina(self):
        s=(self.__a+self.__b+self.__c)/2
        return=math.sqrt((s-a)*(s-b)*(s-c))
class Jednakokracnitrokut(Trokut):
    def __init__ (self,a,b):
        super(Jednakokracnitrokut,self).__init__(self,a,b,c)
    def __str__(self):
        return ("trokut %s%s")%(self.__a,self.__b)
    
        
lista_stranica=[(1,2,3),(3,4,5),(3,4,4),(3,3,3)]
for i in lista_stranica:
        t=Trokut(4,5,6)
        print(repr(t))
    
        
        
        
    
    
            
            
        
        