#include <iostream>
#include <string>
#define NUMRECORD 200 //definisce il numero max di record


/*
1 cercare il nome e cognome del giocatore pi≈≥ vecchio
2 cercare nome cognome e anno del giocatore con meno gol
3 fare la media delle presenze
*/

using namespace std;
int n=0;

class giocatore{
	private:
	string nome;
	string cognome;
	string ruolo; //dif-cen-att-por-trq
	int anno;
	int presenze;
	int gol;
	
	public:
		giocatore(){
			cout<<"inserisci nome\n";
			cin>>nome;
			cout<<"inserisci cognome\n";
			cin>>cognome;
			cout<<"inserisci ruolo(dif-cen-att-por-trq)\n";
			cin>>ruolo;
			cout<<"inserisci anno\n";
			cin>>anno;
			presenze=0;
			gol=0;
		}
		void setNome(string n){
			nome=n;
		}
		string getNome(){
			return nome;
		}
		void setCognome(string n){
			cognome=n;
		}
		string getCognome(){
			return cognome;
		}
		void setAnno(int a){
			anno = a;
		}
		int getAnno(){
			return anno;
		}
		int getPresenze()
		{
			return presenze;
		}
		int getGol(){
			return gol;
		}
		void cambiaRuolo(){
			int r;
			do{
				cout<<"inserisci ruolo \n 1-dif \n 2-cen \n 3-att \n 4-por\n";
				cin>>r;
			}
			while(r<1||r>4);
			switch(r)
			{

				case 1:
					ruolo="dif";
					break;
				case 2:
					ruolo="cen";
					break;
				case 3:
					ruolo="att";
					break;
				case 4:
					ruolo="por";
					break;
				default:
					cout<<"Scelta non permessa!!\n";
			}
		}
		void faGol(int ng){
			gol = gol + ng;
		}
		void faGol(){
			gol = gol + 1;
		}
		void gioca(){
			presenze++;
		}
		void visualizza(){
			cout<<"Giocatore: "<<nome<<" "<<cognome<<endl;
			cout<<"Ruolo "<<ruolo<<endl;
			cout<<"Presenze: "<<presenze<<"\tGol: "<<gol<<endl;
		}
		
};

int main(){
	giocatore ListaG[3];
	string no;
	int scelta=0, r=0, annop, maxg=0;
	do{
		system("cls");
		cout<<"0 ESCI\n";
		cout<<"1 il giocatore gioca\n";
		cout<<"2 il giocatore segna\n";
		cout<<"3 il giocatore segna pi˘ gol\n";
		cout<<"4 modifica il nome del giocatore\n";
		cout<<"5 vedi i dati del giocatore\n";
		cout<<"6 modifica il ruolo del giocatore\n";
		cout<<"7 cerca il giocatore pi˘ vecchio\n";
		cout<<"8 stampa il nome del giocatore con + gol\n";
		cin>>scelta;
		switch(scelta){
			case 0:
				cout<<"Programma terminato\n";
				break;		
			case 1: 
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].gioca();
				break;
			case 2:
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].faGol();
				break;
			case 3:
				int ng;
				cout<<"Quanti gol ha segnato?\n";
				cin>>ng;
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].faGol(ng);
				break;
			case 4:
				cout<<"Inserisci il nuovo nome\n";
				cin>>no;
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].setNome(no);
				break;
			case 5:
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].visualizza();
				break;
			case 6:
				cout<<"inserisci num. giocatore (1,3)\n";
				cin>>r;
				ListaG[r-1].cambiaRuolo();
				break;
			case 7:
				annop=3000;
				for (int i=0;i<3;i++){
					if(ListaG[i].getAnno()<annop){
						annop=ListaG[i].getAnno();
						no=ListaG[i].getNome() + " " + ListaG[i].getCognome();
					}
				}
				cout<<"Il giocatore piu' vecchio e': "<<no<<endl;
				break;
			case 8:
				for (int i=0;i<3;i++){
					if(ListaG[i].getGol()>maxg){
						maxg=ListaG[i].getGol();
						no=ListaG[i].getNome() + " " + ListaG[i].getCognome();
					}
				}
				cout<<"Il giocatore con + gol e': "<<no<<endl;
				break;
			default:
				cout<<"Scelta non consentita\n";
		}
	}
	while(scelta!=0);	
}

