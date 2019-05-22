using System.Collections.Generic;

public class Kata
{

	//
	public static int[] TwoSum(int[] numbers, int target)
	{
		for (int i = 0; i < numbers.Length; i++)
		{
			for (int j = i + 1; j < numbers.Length; j++)
			{
				if (numbers[i] + numbers[j] == target)
					return new int[] { i, j };				
			}
				
		}
					
		return new int[0];
	}	
	
	 //same as python 
	public static int[] TwoSum(int[] numbers, int target)
	{
       Dictionary<int, int> complements = new Dictionary<int, int>();           

       for (int i = 0; i < numbers.Length; i++)
       {
           int num = numbers[i];

           if (complements.ContainsKey(target - num))
           {
               return new int[] { complements[target - num], i };                   
           }

           complements[num] = i;
       }

       return new int[0];
	}
	//too slow
	using System.Linq;
	public int[] TwoSum(int[] nums, int target) {
        
      
        
	  return nums.Select((x,i)=>new [] {i, Array.IndexOf(nums,target-x,i+1)}).First(x => x[1] != -1);
        
    }
}
