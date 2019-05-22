public static int DigitalRoot(int n)
{
      
      int value = n.ToString().Select(x => int.Parse(x.ToString())).Sum();           
      return (value < 10) ? value : DigitalRoot(value);
}

		
		
public class Number
{
  public int DigitalRoot(long n)
  {
     return (int)(1 + (n - 1) % 9);
  }
}