using System;
using System.Linq;

public class Kata 
{
	public static int Test(int[] arr,int n )
        {
            var q = arr.Distinct().OrderBy(x => x).ToList();

            return q.Count() >= n ? q[n-1] : -1;
        }
	
	
}