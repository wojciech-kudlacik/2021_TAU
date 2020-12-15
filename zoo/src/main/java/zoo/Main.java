package zoo;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
	boolean exit;
	ArrayList<String> animals = new ArrayList<String>();
	
	
	public static void main(String[] args) {
		Main main = new Main();
		main.totalWeightOfAnimals(10, 20);
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
				System.out.println("\nEnter the index of animal you want to delete: ");
				try {
					int animalIndex = input.nextInt();
					deleteAnimal(animalIndex);
				} catch(InputMismatchException e) {
					System.out.println("Input is not a number: " + e);
				}
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
		} else if(animals.contains(animal)) {
			System.out.println("Name is already in the list");
		} else if(animal.length() <= 1) {
			System.out.println("Name is too short");
		} else {
			animals.add(animal);
			System.out.println("Animal added");
		}
	}
	
	public void deleteAnimal(int animalIndex) throws IndexOutOfBoundsException {
		int correctIndex = animalIndex - 1; 
		
		if (correctIndex >= 0) {
			try {
				animals.remove(correctIndex);
				System.out.println("Animal removed");
			} catch(IndexOutOfBoundsException e) {
				System.out.println("This index is not available: " + e);
			}
		} else {
			System.out.println("This index is not available");
		}
	}
	
	// New Features - Animal Based calculations
	public void totalWeightOfAnimals(int firstAnimal, int secondAnimal) {
		int result = firstAnimal + secondAnimal;
		
		System.out.println("Both animals weight: " + result);
	}
	 
	
}