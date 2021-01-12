package zoo;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;

class MockitoMainTest {

	// Mocks for the Main class
	@Test
	public void testAnimalHeight() {
		Main main = mock(Main.class);
		when(main.averageAnimalHeight(10f, 20f)).thenReturn(15f);
		float avgHeight = main.averageAnimalHeight(10f, 20f);
		assertEquals(15f, avgHeight);
	}
	
	@Test
	public void testAnimalGender() {
		Main main = mock(Main.class);
		when(main.averageAnimalHeight(10f, 20f)).thenReturn(15f);
	}

}
