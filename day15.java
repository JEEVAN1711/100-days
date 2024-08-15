import java.util.*;
public class Hello {
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in);
        int N1 = sc.nextInt(); 
        int N2 = sc.nextInt();
        for (int ctr1 = 1; N1 <= N2; ctr1++) {
            for (int ctr2 = N1; ctr2 <= N2; ctr2++) { 
                System.out.print(ctr2 + " ");
            }
            System.out.println();
            N2--;
            
        }
        
    }
}
