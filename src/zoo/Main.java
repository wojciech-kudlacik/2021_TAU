package zoo;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	boolean exit;
	
	
	public static void main(String[] args) {
		Main main = new Main();
		main.runMenu();
	}
	
	
	public void runMenu() {
		while (!exit) {
			menu();
			int choice = getUserInput();
			selectAction(choice);
		}
	}
	
	public void menu() {
      System.out.println("\nSuper Awesome Zoo Menu");
      System.out.println("----------------------");
      System.out.println("1 - List animals");
      System.out.println("2 - Add animal");
      System.out.println("3 - Delete animal");
      System.out.println("0 - Quit");
	}
	
	public int getUserInput() {
		int choice = -1;
		Scanner input = new Scanner(System.in);
		
		while(choice < 0 || choice > 3) {
			try {
				System.out.print("\nEnter your selection: ");
				choice = Integer.parseInt(input.nextLine());
			}
			catch(NumberFormatException e) {
				System.out.println("\nInvalid selection" + e);
			}
		}
		return choice;
	}
	
	public void selectAction(int choice) {
		switch(choice) {
			case 0:
				exit = true;
				System.out.println("See you later, aligator");
				break;
			case 1:
				System.out.println("LIST");
				break;
			case 2:
				System.out.println("ADD");
				break;
			case 3:
				System.out.println("DELETE");
				break;
			default:
				System.out.println("UNKNOWN ERR");
				
		}
	}
	
//	
//	private static void addAnimal(String animal) {
//		
//		if (animal.matches(".*\\d.*")) {
//			System.out.println("Name can't contain numbers");
//		} else {
//			animals.add((String) animal);
//			System.out.println("Animal added");
//		}
//	}
}