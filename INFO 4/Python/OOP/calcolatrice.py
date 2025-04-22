class calcolatrice:

    __primo = 0
    __secondo = 0
    __operaz=""

    def __init__(self, __p, __s, __o):
        self.__primo=__p
        self.__secondo=__s
        self.__operaz=__o
    
    def passavalori(self, a, b):
        __primo = a
        __secondo = b

    def somma(self):
        return __primo + __secondo
    
    def differenza(self):
        return __primo - __secondo
    
    def prodotto(self):
        return __primo * __secondo
    
    def quoziente(self):
        if secondo==0:
            return 0
        return __primo / __secondo
    
    
