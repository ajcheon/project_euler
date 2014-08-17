import java.util.ArrayList;


public class ProjectEuler5 {

   /**
    * @param args
    */
   public static void main(String[] args) {
      int currentNum = 2;
      while(true){
         if(divisBy1to20(currentNum) == true){
            System.out.println("LowestValue is: " + currentNum);
            break;
         }
         currentNum++;
      }
   }

   public static boolean divisBy1to20(int n){
      ArrayList<String> factors = new ArrayList<String>();
      int range = 20;
      
      for (int i = 1; i <= range; i++) {
         if(n % i == 0){
            factors.add("");
         }
      }
      
      if(factors.size() == range){
         return true;
      }else{return false;}
      
   }
   
}