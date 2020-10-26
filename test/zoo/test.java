package zoo;

import org.junit.After;
import org.junit.Before;
import org.junit.jupiter.api.Test;

class test {
	
	@Before
	public void setUp() {
		System.out.println("BEFORE");

	}
	
	@After
	public void tearDown() {
		System.out.println("AFTER");

	}

	@Test
	public void test() {
		System.out.println("TEST");
	}

}
