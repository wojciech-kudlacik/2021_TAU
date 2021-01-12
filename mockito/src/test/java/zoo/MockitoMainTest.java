package zoo;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class MockitoMainTest {

	private Main mockMain;
	
	// Mocks for the Main class
    @BeforeEach
    public void init() {
    	mockMain = mock(Main.class);
    	when(mockMain.averageAnimalHeight(10f, 20f)).thenReturn(15f);
    	when(mockMain.animalGender('M')).thenReturn('M');
    	int[] animalsWeight = new int[3]; 
    	when(mockMain.averageWeightOfAnimals(animalsWeight)).thenReturn(60.0);

    }

    @AfterEach
    public void tearDown() {
    	
    }
	
	@Test
	public void testAnimalHeight() {
		float avgHeight = mockMain.averageAnimalHeight(10f, 20f);
		assertEquals(15f, avgHeight);
	}
	
	@Test
	public void testAnimalGender() {
		char gender = mockMain.animalGender('M');
		assertEquals('M', gender);
	}
	
	@Test
	public void testAnimalAvgWeight() {
		int[] animalsWeight = new int[3];
		double avgWeight = mockMain.averageWeightOfAnimals(animalsWeight);
		assertEquals(60.0, avgWeight);
	}

}
