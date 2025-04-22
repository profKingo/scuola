class contoCorrente:
    _nome=""
    _nconto=0
    _saldo=0

    def __init__(self):
        self._nome="XXX"
        self._nconto=100
        self._saldo=0
    
    def __init__(self, n, c, s):
        self._nome=n
        self._nconto=c
        self._saldo=s
    
    def stampaConto(self):
        print("Conto:" + str(self._nconto))
        print("Titolare:" + str(self._nome))
        print("Saldo:" + str(self._saldo))
    def versa(self, imp):
        self._saldo += imp
    def preleva(self, imp):
        self._saldo -= imp

class Libretto(contoCorrente):
    _interesse=0

    def __init__(self, n, c, s, inte):
        super().__init__(n,c,s)
        self._interesse=inte
    
    def calcolaint(self):
        self._saldo=self._saldo*(1+self._interesse/100)
        
c = contoCorrente("Cicco", 3415, 900) 
c.stampaConto()
c.versa(200)
c.stampaConto()
c.preleva(300)
c.stampaConto()
l = Libretto("LibCicco", 1114, 900, 3)
l.stampaConto()
l.calcolaint()
l.stampaConto()

'''
class Serbatoio:
    tipo
    qtamax
    qtapres

    carico()
    scarico()
    stamparesiduo()  '''