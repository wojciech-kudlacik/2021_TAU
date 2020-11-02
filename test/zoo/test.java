package zoo;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class test {
	
	private Main main = new Main();
	
	@BeforeEach
	public void setUp() {
		main.addAnimal("Leon");
		main.addAnimal("Felix");
		main.addAnimal("Dumbo");
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
	public void testListA() {
		String[] expectedList = {"Leon", "Felix", "Dumbo"};
		String[] actualList = main.animals.toArray(new String[0]);
		assertArrayEquals(expectedList, actualList);
		
	}
	

}
