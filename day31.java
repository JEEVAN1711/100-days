import java.util.Scanner;
public class age{
    public static void main(String[] args) {
        Scanner jeev = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = jeev.nextInt();
        if (age >= 0 && age <= 12)
        {
            System.out.println("Child");
        }
        else if (age >= 13 && age <= 35) 
        {
            System.out.println("Youth");
        } 
        else if (age > 35 && age <= 60) 
        {
            System.out.println("Adult");
        } 
        else
        {
            System.out.println("Invalid Age");
        }
        jeev.close();
    }
}
