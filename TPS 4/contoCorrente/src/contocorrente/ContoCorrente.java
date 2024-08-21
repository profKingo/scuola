/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package contocorrente;

/**
 *
 * @author cicco
 */
public class ContoCorrente {

    private String nome;
    private int numconto;
    private double saldo;
    /**
     * @param args the command line arguments
     */
    public ContoCorrente(){
        nome="";
        numconto=9999;
        saldo=0;
    }
    public ContoCorrente(String n, int c, int s){
        nome=n;
        numconto=c;
        saldo=s;
    }

    public void versa(int s){
        saldo+=s;
    }

    public void preleva(int s){
        if (saldo>=s){
            saldo-=s;
        }
        else{
            System.out.println("Saldo non sufficiente! puoi prelevare fino a: " + saldo);
            saldo=0;
        }
    }
    void stampaConto(){
        System.out.println("Conto       " + numconto);
        System.out.println("Intestato a " + nome);
        System.out.println("Saldo conto " + saldo);
    }
    public static void main(String[] args) {
        // TODO code application logic here
    }
    
}
