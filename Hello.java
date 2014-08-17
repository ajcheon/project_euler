public class Problem3{
	public static Boolean[] populate(Boolean[] list, long n){
		long cap1 = (long)(Math.ceil(n));
		long cap2 = n;
		int i = 0;

		while (i <= cap1){
			list[i] = true;
			i++;
		}

		System.out.println("i is now" + i);
		return null;
	}


	public static void main(String[] args){
		long limit = 600851475143L;
		System.out.println(Integer.MAX_VALUE);
		//Boolean[] nums = new Boolean[limit];
		//populate(nums, limit);
		//System.out.println(nums.size());
	}
}