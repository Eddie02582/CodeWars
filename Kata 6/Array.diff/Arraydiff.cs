using System.Linq;
using System.Collections.Generic;
public class Kata
{
  public static int[] ArrayDiff(int[] a, int[] b)
  {
    return a.Where(n => !b.Contains(n)).ToArray();
  }
  
    public static int[] ArrayDiff_(int[] a, int[] b)
    {
      List<int> result = new List<int>();
       foreach (int x in a)
       {
           bool Isin = false;
           foreach (int y in b)
           {
               if (y == x)
               {
                   Isin = true;
                   break;
               }
           }
           if (!Isin)
               result.Add(x);
       }
       return result.ToArray();
    } 
	
	public static int[] ArrayDiff__(int[] a, int[] b)
	{
		//like python set(b)
		var sb = new HashSet<int>(b);
		return Array.FindAll(a, x => !sb.Contains(x));
	}
}