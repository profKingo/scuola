import threading

# Definiamo una risorsa condivisa
caramelle = 10

# Definiamo un lock mutex
mutex = threading.Lock()

def prendi_caramella():
    global caramelle
    # Acquisiamo il lock mutex
    mutex.acquire()
    try:
        # Verifichiamo se ci sono ancora caramelle nella scatola
        if caramelle > 0:
            print("Prendo una caramella!")
            caramelle -= 1
        else:
            print("Mi dispiace, non ci sono più caramelle!")
    finally:
        # Rilasciamo il lock mutex
        mutex.release()

# Creiamo tre thread e li avviamo
t1 = threading.Thread(target=prendi_caramella)
t2 = threading.Thread(target=prendi_caramella)
t3 = threading.Thread(target=prendi_caramella)
t1.start()
t2.start()
t3.start()
# Attendiamo che tutti i thread terminino l'esecuzione
t1.join()
t2.join()
t3.join()