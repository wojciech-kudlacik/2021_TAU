package zoo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	boolean exit;
	ArrayList<String> animals = new ArrayList<String>();
	
	
	public static void main(String[] args) {
		Main main = new Main();
		main.runMenu();
	}
	

	//MENU
	
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
		Scanner input = new Scanner(System.in);
		
		switch(choice) {
			case 0:
				exit = true;
				System.out.println("See you later, aligator");
				break;
			case 1:
				listAnimals();
				break;
			case 2:
				System.out.println("\nEnter the name of an animal: ");
				String animal = input.nextLine();
				addAnimal(animal);
				break;
			case 3:
				System.out.println("DELETE");
				break;
			default:
				System.out.println("UNKNOWN ERR");
				
		}
	}
	
	
	//OPERATIONS
	
	public void listAnimals() {
		System.out.println("\nList of all animals:");
		animals.forEach(System.out::println);
	}
	
	public void addAnimal(String animal) {
		if (animal.matches(".*\\d.*")) {
			System.out.println("Name can't contain numbers");
		} else {
			animals.add(animal);
			System.out.println("Animal added");
		}
	}
	
	
}