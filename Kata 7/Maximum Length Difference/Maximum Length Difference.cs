using System;
using System.Linq;

public class MaxDiffLength 
{
    
    public static int Mxdiflg(string[] a1, string[] a2) 
    {
        if(a1.Length <= 0 || a2.Length <= 0)
          return -1;   
        var first = Math.Abs(a1.Max(x => x.Length) - a2.Min(x => x.Length));
        var second = Math.Abs(a2.Max(x => x.Length) - a1.Min(x => x.Length));
        return Math.Max(first, second);
    }
	
	 public static int Mxdiflg(string[] a1, string[] a2)
     {
         // your code
         if (a1.Count() == 0 || a2.Count() == 0)
             return 0;
     
         var q1 = a1.Select(x => x.Count());
         int max_a1 = q1.ToList().Max();
         int min_a1 = q1.ToList().Min();
     
         var q2 = a2.Select(x => x.Count());
         int max_a2 = q2.ToList().Max();
         int min_a2 = q2.ToList().Min();
     
         return Math.Max(Math.Abs(max_a1 - min_a2), Math.Abs(max_a2 - min_a1));
     }
}