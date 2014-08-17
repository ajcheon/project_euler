/* WE MUST GO WITH THE JAVA VERSION FOR PROBLEM 3!
 * 1/6/13
 */

/*public class Problem3{
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
		System.out.println(Long.MAX_VALUE);
		//Boolean[] nums = new Boolean[limit];
		//populate(nums, limit);
		//System.out.println(nums.size());
	}
}*/
import java.util.*;
public class Problem3{
	public static Boolean[] populate(ArrayList<Boolean> list, long n){
		//long cap1 = (long)(Math.ceil(n));
		//long cap2 = n;
		int i = 0;
		while (i <= n){
			list.add(true);
			i++;
		}

		System.out.println("Length of arraylist: " + list.size());
		return null;
	}


	public static void main(String[] args){
		long limit = 100;
		//System.out.println(Long.MAX_VALUE);
		ArrayList<Boolean> nums = new ArrayList(); // should grow as we go
		populate(nums, limit);
		//System.out.println(nums.size());
	}
}