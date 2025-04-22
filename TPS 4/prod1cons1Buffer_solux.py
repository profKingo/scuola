# importazione libreria per i thread e lock
from threading import Thread, BoundedSemaphore
from Buffer import Buffer 
import time
import random
# definizione oggetto Buffer  
buffer1 = Buffer()
FINE = -1 

class Produttore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    def run(self):
        for index in range(4):
            dato = random.randint(10, 99) 
            print(self.nome," Prodotto : ", dato, " (", index+1, " di 4 )")
            buffer1.setdato(self.nome, dato)
            time.sleep(random.randint(1,3))
  
        buffer1.setdato(self.nome, FINE) 
    
class Consumatore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    def run(self):
        dato = 0
        while dato is not FINE:
            dato = buffer1.getdato(self.nome)
            if dato is not FINE:
                print(self.nome," Consumato: ", dato) 
                time.sleep(random.randint(1, 6))
            else:
                print("FINE ESECUZIONE!")
    
# creazione dei thread
buffer = 0
thread1 = Produttore("Scrive1")
thread2 = Consumatore("Legge1")
thread3 = Produttore("Scrive2")
thread4 = Consumatore("Legge2")
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("\nFine esecuzione")

 


