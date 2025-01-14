#include <cstdlib>
#include <iostream>
#include <iomanip>
# include "Persona.h"

//namespace inserito da dev C++
using namespace std;

class Sportivo : public Persona {
  protected:
    string sport;
	public: 
    Sportivo(string nom, string cog, string spo) : Persona(nom,cog) { 
    sport = spo;
  }
  void stampa() { 
    cout << "Nome     : " << nome << endl;
    cout << "Cognome  : " << cognome << endl;
    cout << "sport    : " << sport << endl;
  }
};
int main() {
	// istanza di Sportivo
	cout << endl << "Sportivo" << endl << "------" << endl;
	Sportivo s("Rossi","Valentino", "motociclismo");
	s.stampa();
}

