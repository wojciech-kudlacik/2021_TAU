package zoo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class MockitoTest {

	// Mocks for the Animal class
	@Test
	public void testNumberOfLegs() {
		Animal animal = mock(Animal.class);
		when(animal.getNoOfLegs()).thenReturn(4);
		int legs = animal.getNoOfLegs();
		assertEquals(4, legs);
	}
	
	@Test
	public void testIsAnimalVegetarian() {
		Animal animal = mock(Animal.class);
		when(animal.isVegetarian()).thenReturn(false);
		boolean isVege = animal.isVegetarian();
		assertFalse(isVege);
	}
	
	@Test
	public void testAnimalFood() {
		Animal animal = mock(Animal.class);
		when(animal.getEats()).thenReturn("Food");
		String eats = animal.getEats();
		assertEquals("Food", eats);
	}
	
	
	
//	@Test
//	public void testAnimalLegs() {
//		int expected = 2;
//		int actual = animal.getNoOfLegs(); 
//		assertEquals(expected, actual);
//	}
	

}
