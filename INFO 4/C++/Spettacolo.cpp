#include <iostream>
using namespace std;
class spettacolo{
	private:
		string titolo;
		string genere;
		int numSpettatori;
		int repliche;
		int punteggio;
	public:
		spettacolo(){
			cout<<"inserisci titolo"<<endl;
			cin>>titolo;
			cout<<"inserisci genere"<<endl;
			cin>>genere;
			cout<<"inserisci numero spettatori"<<endl;
			cin>>numSpettatori;
			cout<<"inserisci numero repliche"<<endl;
			cin>>repliche;
			cout<<"inserisci punteggio"<<endl;
			cin>>punteggio;
		}
		spettacolo(string t, string g, int ns, int r, int p){
			titolo=t;
			genere=g;
			numSpettatori=ns;
			repliche=r;
			punteggio=p;
		}
		string getTitolo(){
			return titolo;
		}
		string getGenere(){
			return genere;
		}
		int getNumSpett(){
			return numSpettatori;
		}
		int getRepliche(){
			return repliche;
		}
		int getPunteggio(){
			return punteggio;
		}
		void setTitolo(string t){
			titolo=t;
		}
		void setGenere(string g){
			genere=g;
		}
		void daiVoto(int voto){
			punteggio=voto;
		}
		void proietta(int spett){
			repliche++;
			numSpettatori+=spett;
		}
};

int main() {
	string nome="Wish", genere="Animazione";
	spettacolo *Wish;
	Wish = new spettacolo(nome, genere,0,0,7);
	Wish->proietta(3000);
	Wish->daiVoto(9);
	Wish->proietta(4000);
	cout<<"Spettatori di Wish: "<<Wish->getNumSpett()<<endl;
	return 0;
}
