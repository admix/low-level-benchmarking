package ca.admix.application;

public class Application {

	public static void main(String[] args) {
		
		System.out.println("Hello");
		SieveJava(10);
	}
	
	private static void SieveJava(int maxNum) {
	  int i, j;
	  boolean[] Data = new boolean[maxNum+1];
	
	  for (i=2; i<=maxNum; i++) {
	      Data[i] = true;
	  }
	
	  for (i=2; i<=maxNum; i++) {
	      if (Data[i]) {
	          for (j=i+i; j<=maxNum; j+=i) {
	              Data[j]= false;
	          }
	      }
	  }
	}
}
