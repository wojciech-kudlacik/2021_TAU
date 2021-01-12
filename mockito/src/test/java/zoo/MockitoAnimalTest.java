package zoo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class MockitoAnimalTest {
	
	private Animal mockAnimal;

	// Mocks for the Animal class
    @BeforeEach
    public void init() {
    	mockAnimal = mock(Animal.class);
    	when(mockAnimal.getNoOfLegs()).thenReturn(4);
    	when(mockAnimal.isVegetarian()).thenReturn(false);
    	when(mockAnimal.getEats()).thenReturn("Food");
    }

    @AfterEach
    public void tearDown() {
    	
    }
	
	@Test
	public void testNumberOfLegs() {
		int legs = mockAnimal.getNoOfLegs();
		System.out.println(legs);
		assertEquals(4, legs);
	}
	
	@Test
	public void testIsAnimalVegetarian() {
		boolean isVege = mockAnimal.isVegetarian();
		assertFalse(isVege);
	}
	
	@Test
	public void testAnimalFood() {
		String eats = mockAnimal.getEats();
		assertEquals("Food", eats);
	}
	


}
