/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package matrice;
import java.util.Scanner;

/**
 *
 * @author cicco
 */
public class Matrice {

    public int nrighe;
    public int ncolonne;
    public int mat[][];
    public Scanner in;
    
    public Matrice(){
        ncolonne=3;
        nrighe=3;
        mat=new int[nrighe][ncolonne];
        in = new Scanner(System.in);
    }
    
    public Matrice(int r, int c){
        nrighe=r;
        ncolonne=c;
        mat=new int[nrighe][ncolonne];
        in = new Scanner(System.in);
    }
    
    public void riempiRiga(){
        for(int i=0;i<nrighe;i++){
            for(int j=0;j<ncolonne;j++){
                System.out.println("inserisci valore");
                int n = in.nextInt();
                mat[i][j]=n;
            }
        }
    }
    
    public void riempiCol(){
        for(int j=0;j<ncolonne;j++){
            for(int i=0;i<nrighe;i++){
                System.out.println("inserisci valore");
                int n = in.nextInt();
                mat[i][j]=n;
            }
        }
    }
    
    public int cercaMax(int m[][]){
        int max=0;
        for(int i=0;i<nrighe;i++){
            for(int j=0;j<ncolonne;j++){
                if (m[i][j]>max){
                    max=m[i][j];
                }
            }
        }
        return max;
    }
    
    public int cercaMaxCol(int m[][], int col){
        int maxc=0;
        for(int i=0;i<nrighe;i++){
            if (m[i][col]>maxc){
                    maxc=m[i][col];
            }
        }
        ///implementa la ricerca del max su m alla colonna col
        return maxc;
    }
    public int cercaMaxRiga(int m[][], int riga){
        int maxr=0;
        for(int j=0;j<ncolonne;j++){
            if (m[riga][j]>maxr){
                maxr=m[riga][j];
            }
        }///implementa la ricerca del max su m alla riga riga
        return maxr;
    }
    /**
     * @param args the command line arguments
     */
    public void stampaMaxRiga(int m[][]){
        for(int i=0;i<nrighe;i++){
            int max=0;
            for(int j=0;j<ncolonne;j++){
                if (m[i][j]>max){
                    max=m[i][j];
                }
            }    
            System.out.println("Il valore massimo della riga " + i + " vale " + max);
        }
    }
    public void stampaMat(int m[][]){
        for(int i=0;i<nrighe;i++){
            for(int j=0;j<ncolonne;j++){
                System.out.print(m[i][j] +  "\t");
            }    
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Matrice m = new Matrice();
        m.riempiCol();
        m.stampaMat(m.mat);
        m.stampaMaxRiga(m.mat);
        System.out.println("Il Massimo della matrice è: " + m.cercaMaxCol(m.mat, 2));
        System.out.println("Il Massimo della matrice è: " + m.cercaMax(m.mat));
    }
    
}
