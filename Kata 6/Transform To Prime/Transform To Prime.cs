using System;
using System.Linq;

/*
 Find 
1- minimumNumber ({3,1,2}) ==> return (1)
sum(3,1,2) ->6
next prime num is 7

so return 7-6

*/
namespace TransformToPrime
{
  class Solution
  {   

	public static int MinimumNumber(int[] numbers, int n = 0)
    {
        if (IsPrime(numbers.Sum() + n)) return n;
        return MinimumNumber(numbers, ++n);
    }
    static bool IsPrime(int n)
    {
        if (n == 1) return false;
        if (n == 2) return true;
        return Enumerable.Range(2, (int)Math.Sqrt(n)).All(x => n % x > 0);
    }
    public static int MinimumNumber_(int[] numbers)
    {
		int sum=numbers.Sum();		
		int n=sum;
		while(Enumerable.Range(2, (int)Math.Sqrt(n)).Any(x => n % x ==0))
			n++;		
		return sum-n;		
	}	
      
  }
}













