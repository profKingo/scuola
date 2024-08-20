/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package atleta;

/**
 *
 * @author cicco
 */
public class Atleta {

    private String nome;
    private String cognome;
    private String disciplina;
    private int medaglie;
    private String tipomed[];
    private int anno;
    
    public Atleta(String n, String c, String d, int m, int a){
        nome=n;
        cognome=c;
        disciplina=d;
        medaglie=m;
        tipomed=new String[20];
        anno=a;
    }
    public void assegnaMedaglia(String tipo){
        medaglie++;
        tipomed[medaglie-1]=tipo;
    }
    public void descAtleta(){
        System.out.println("###### ATLETA #######");
        System.out.println(nome + " " + cognome + " Anno: " + anno);
        System.out.println("# medaglie: " + medaglie);
        int v[]=stat(tipomed);
        System.out.println("# Oro:         " + v[0]);
        System.out.println("# Argento: " + v[1]);
        System.out.println("# Bronzo:   " + v[2]);
    }
    public int[] stat(String v[]){
        int oro=0, arg=0, bro=0, ris[];
        ris = new int[3];
        for(int i=0;i<medaglie;i++){
            if (v[i].equalsIgnoreCase("oro"))
                oro++;
            if (v[i].equalsIgnoreCase("argento"))
                arg++;
            if (v[i].equalsIgnoreCase("bronzo"))
                bro++;
        }
        ris[0]=oro;
        ris[1]=arg;
        ris[2]=bro;
        return ris;
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Atleta a = new Atleta("Gino", "Caccamo", "Nuoto", 0, 2000);
        a.assegnaMedaglia("oro");
        a.assegnaMedaglia("bronzo");
        a.assegnaMedaglia("argento");
        a.assegnaMedaglia("oro");
        a.descAtleta();
        Atleta Edo = new Atleta("","","",0,2005);
    }
    
}
