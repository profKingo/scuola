#include <ctime>
#include <iostream> 
#include <cstdlib>
#include <iomanip>
#include <string.h>
#include <cstring>   

using namespace std;

#include "Persona.h"
class Sportivo : public Persona{
protected:
  string sport;
public: 
  Sportivo() {};
  Sportivo(string nom, string cog, string spo): Persona(nom, cog){
		sport = spo;
	}
  void stampa() { 
	Persona::stampa(); // metodo del padre
    cout << "sport    : " << sport << endl;
  }
};