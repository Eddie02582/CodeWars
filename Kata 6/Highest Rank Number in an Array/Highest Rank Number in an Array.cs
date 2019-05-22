using System.Linq;
public class Kata
{
	  public static int HighestRank(int[] arr)
	  {
		return arr.GroupBy(x => x).OrderBy(g => g.Count()).ThenBy(g => g.Key).Last().Key;
	  }
	  
	  public static int HighestRank(int[] arr)
	  {
		return arr.GroupBy(x => x).OrderByDescending(g => g.Count()).ThenByDescending(g => g.Key).First().Key;
	  }
	  public static int HighestRank(int[] arr)
	  {
			return arr
			  .GroupBy(i => i)
			  .OrderByDescending(gr => gr.Count())
			  .ThenByDescending(gr => gr.Key)
			  .Select(gr => gr.Key)
			  .First();
	}
}