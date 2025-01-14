#include <vector>
#include <iostream>
using namespace std;

int main()
{
    int i, n;
    vector<int> v;
    cout<<"Inserisci numero elementi vettore: "<<endl;
    cin>>n;
    for (i=0;i<n;i++){
        v.push_back(i);
    }
    for (i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }
    v.back();//ritorna il primo elemento
    v.front();//ritorna l'ultimo elemento
    v.pop_back();//elimina ed estrae l'ultimo elemento
    v.begin();//indice iniziale
    v.end();//indice finale
    v.insert(v.begin(),8);// inserisce all'inizio (o alla posizione che voglio con +x) un valore (8)
    
} // namespace std;
