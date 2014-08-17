public class Problem3Brute{

	public static Boolean isPrime(long n){
		for (long i = 1; i <= n; i++){
			if (n % i == 0 && i != 1 && i != n){
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args){
		long limit = 600851475143L;
		for (long i = (long)(Math.ceil(Math.sqrt(limit))); i >= 1; i--){
			if (limit % i == 0){
				System.out.println("Divisible by " + i);
				if (isPrime(i)){
					System.out.println(i + "is prime");
				}
			}
		}
	}
}