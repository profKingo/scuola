#include <iostream>
#include <string>
using namespace std; 

class dispenser{
    private:
    int capienza;
    int qtdisp;
    int qtaerogata;
    string modello;
    public:
    dispenser(){
        cout<<"inserisci la qta massima(500=standard): \n";
        cin>>capienza;
        cout<<"inserisci la qta erogata(10=standard): \n";
        cin>>qtaerogata;
        cout<<"inserisci il modello: \n";
        cin>>modello;
        qtdisp=0;
    }
    dispenser(int c, int er, string m){
        modello=m;
        capienza=c;
        qtaerogata=er;
        qtdisp=0;
    }
    string getmodello(){
        return modello;
    }
    void setmodello(string m){
        modello=m;
    }
    int getcapienza(){
        return capienza;
    }
    void setcapienza(int c){
        capienza=c;
    }
    int geterogazione(){
        return qtaerogata;
    }
    void seterogazione(int c){
        qtaerogata=c;
    }
    void push(){
        if (qtdisp>=qtaerogata){
            qtdisp-=qtaerogata;
        }
        else 
            qtdisp=0;
        cout<<"Quantita presente in "<<modello<<": "<<qtdisp<<" cl \n";
    }
    void ricarica(){
        int c;
        cout<<"Quanto ricarichi? \n";
        cin>>c;
        if (c>capienza-qtdisp){
            cout<<"Ne hai messo troppo!!\n";
            qtdisp=capienza;
        }
        else{
            qtdisp+=c;
        }
        cout<<"Ricarica su "<<modello<<" effettuata!\n";
    }
};
int main(){
    dispenser d1;
    dispenser d2(400,8,"risparmioso");
    d1.ricarica();
    d2.ricarica();
    for(int i=0;i<3;i++){
    	d1.push();
	}
    for(int i=0;i<3;i++){
    	d2.push();
	}
    return 0;
}