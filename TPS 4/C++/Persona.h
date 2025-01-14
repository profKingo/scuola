#include <ctime>
#include <iostream> 
#include <cstdlib>
#include <iomanip>
#include <string.h>
#include <cstring>  
using namespace std;

class Persona{
protected:
	string cognome;
	string nome;
public:
  Persona(){};
	Persona(string no, string co){
		nome = no;
		cognome = co;
	};
	~Persona(){};
	void setNome(string no) {
	  nome = no;
	};
	void setCognome(string co){
		cognome = co;
	};
	string getCognome(){
		return cognome;
	};
	string getNome(){
		return nome;
	};
  void stampa(){ 
   cout << "Nome     : " << nome << endl;
   cout << "Cognome  : " << cognome << endl; 
  };
};


