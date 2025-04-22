# importazione libreria per i thread e lock
from threading import Thread, BoundedSemaphore
import random
# definizione oggetto mutex
nrThread = 1
semaforo = BoundedSemaphore(value = nrThread)
def set_dato(valore):
  global dato 
  dato = valore
def get_dato():
  return dato

class Produttore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    def run(self):
        semaforo.acquire()
        # attivita' svolta dal thread
        buffer = random.randint(10, 99) 
        set_dato(buffer)
        print ("\nprodotto ", buffer)
        semaforo.release()
        
class Consumatore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    def run(self):
        semaforo.acquire()
        buffer = get_dato()
        print ("\nconsumato ", buffer)
        set_dato(0)
        semaforo.release()

# creazione dei thread
thread1 = Produttore("Scrive")
thread2 = Consumatore("Legge")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("\nFine esecuzione")

 


