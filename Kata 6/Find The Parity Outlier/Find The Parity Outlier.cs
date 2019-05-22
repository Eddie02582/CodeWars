using System.Linq;

public class Kata
{
  public static int Find(int[] integers)
  {
    var evenNumbers = integers.Where(integer => integer % 2 == 0);
    var oddNumbers = integers.Where(integer => integer % 2 == 1);
    return evenNumbers.Count() == 1 ? evenNumbers.First() : oddNumbers.First();
  }
  
   public static int Find(int[] integers)
  {
    return integers.Where(x => x % 2 == 0).Count() == 1 ? integers.Where(x => x % 2 == 0).First() : integers.Where(x => x % 2 != 0).First(); 
  }
}