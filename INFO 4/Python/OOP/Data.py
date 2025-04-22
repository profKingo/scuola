class Data(object):
    __g=0
    __m=0
    __a=0
    ''''''
    giorni=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    def __init__(self, __g, __m, __a):
        self.__g=__g
        self.__m=__m
        self.__a=__a
        if self.bisestile():
            self.giorni[2]=29
    
    def __str__(self):
        return str(self.__g) + "/" + str(self.__m) + "/" + str(self.__a)
    
    def __add__(self, gg):
        self.__g+=gg
        while self.__g > self.giorni[self.__m]:
            self.__g-=self.giorni[self.__m]
            self.__m+=1
            while self.__m>12:
                self.__m-=12
                self.__a+=1
                if self.bisestile():
                    self.giorni[2]=29
                else:
                    self.giorni[2]=28
        return self
    
    def __int__(self):
        if self.__a==0:
            annozero=0
        else:
            annozero=1
        anni = annozero + self.__a * 365 \
            + int((self.__a - 1)/4)\
                -int(((self.__a)/4)) + int((self.__a)/400)
        mesi=0
        for k in range(1, self.__m):
            mesi+=self.giorni[k]
        return anni + mesi + self.__g

    def bisestile(self):
        if self.__a%400==0 or ((self.__a%100!=0) and (self.__a%4==0)):
            return True
        else:
            return False

