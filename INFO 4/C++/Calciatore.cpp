#include <ctime>
#include <iostream> 
#include <cstdlib>
#include <iomanip>
#include <string.h>
#include <cstring>   
using namespace std;

#include "Sportivo.h"
class Calciatore : public Sportivo{
protected:
  string squadra;
  string ruolo;
public: 
  Calciatore(string no, string co, string sp, string sq): 
	Sportivo(no, co, sp){
	squadra = sq;
  }
  void stampa(){ 
		Sportivo::stampa();
		cout << "squadra  : " << squadra << endl;
  }
  void stampaSquadra() {
		cout << "squadra  : " << squadra << endl;
	}
};

int main() {
  	// istanza di Persona
	Persona p("Alberto", "Sordi");
	cout << endl << "Persona" << endl << "-------" << endl;
	p.stampa();

	// istanza di Sportivo
	cout << endl << "Sportivo" << endl << "------" << endl;
	Sportivo s("Rossi","Valentino", "motociclismo");
	s.stampa();

	// istanza di Calciatore
	cout << endl << "Calciatore" << endl << "----" << endl;
	Calciatore c("Diego", "Maradona", "calcio", "napoli");
	c.Sportivo::stampa();   // metodo del padre Sportivo
	c.stampaSquadra();      // metodo della classe Calciatore
		
	system("pause");
}


