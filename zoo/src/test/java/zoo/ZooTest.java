package zoo;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ZooTest {
	
	private Main main = new Main();
	
	@BeforeEach
	public void setUp() {
		main.addAnimal("Leon");
		main.addAnimal("Felix");
		main.addAnimal("Dumbo");
		Main.animalsWeight[0] = 10;
		Main.animalsWeight[1] = 20;
		Main.animalsWeight[2] = 30;
	}
	
	@AfterEach
	public void tearDown() {

	}
	
	@Test
	public void testAddAnimals() {
		int expected = 3;
		int actual = main.animals.size(); 
		assertEquals(expected, actual);
	}
	
	@Test
	public void testList() {
		String[] expectedList = {"Leon", "Felix", "Dumbo"};
		String[] actualList = main.animals.toArray(new String[0]);
		assertArrayEquals(expectedList, actualList);
		
	}
	
	@Test void testAll() {
		String expectedValue1 = "Leon";
		String actualValue1 = main.animals.get(0);
		
		String expectedValue2 = "Felix";
		String actualValue2 = main.animals.get(1);
		
		assertAll("Should return animals at their specific indexes: ",
				() -> assertEquals(expectedValue1, actualValue1),
				() -> assertEquals(expectedValue2, actualValue2)
			);
	}
	
	// New tests
	
	@Test void testDeleteAnimal() {
		boolean actual = main.deleteAnimal(2);
		assertEquals(true, actual);
	}
	
	@Test void testDeleteAnimalIncorectIndex() {
		boolean actual = main.deleteAnimal(4);
		assertEquals(false, actual);
	}
	
	@Test void animalsWeightLength() {
		assertEquals(Main.animalsWeight.length, 3);
	}
	
	@Test void testTotalWeightOfAnimalsBool() {
		int firstAnimal = 20;
		int secondAnimal = 10;
		int result = main.totalWeightOfAnimals(firstAnimal, secondAnimal);
		assertTrue(result == 30);
	}
	
	@Test void testTotalWeightOfAnimals() {
		int firstAnimal = 20;
		int secondAnimal = 10;
		int result = main.totalWeightOfAnimals(firstAnimal, secondAnimal);
		assertEquals(result, 30);
	}
	
	@Test void testTotalWeightOfMoreThanTwoAnimals() {
		int result = main.totalWeightOfMoreThanTwoAnimals(Main.animalsWeight);
		assertEquals(result, 60);
	}
	
	@Test void testAverageWeightOfAnimals() {
		double expected = 20.0;
		double result = main.averageWeightOfAnimals(Main.animalsWeight);
		
		assertEquals(expected, result); 

	}
		

//  How an unhandled exception might be dealt with: 	
//	@Test
//	public void testDeleteAnimalException() {
//		assertThrows(IndexOutOfBoundsException.class, () -> main.deleteAnimal(4));
//	}

}