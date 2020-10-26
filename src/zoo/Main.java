package zoo;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	static ArrayList<String> animals = new ArrayList<String>();
	
	public static void main(String[] args) {
		
		Scanner inputScanner = new Scanner(System.in);
		
		while(true) {
			
			System.out.println("Enter animal name: ");
			String animal = inputScanner.nextLine();
			addAnimal(animal);
		}
		
	}
	
	private static void addAnimal(String animal) {
		animals.add(animal);
	}
}
