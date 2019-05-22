using System;

public class Kata
{
	  public static string Rot13(string message)
	  {
		string result = "";
				foreach (var s in message)
				{
					if ((s >= 'a' && s <= 'm') || (s >= 'A' && s <= 'M'))
						result += Convert.ToChar((s + 13)).ToString();
					else if ((s >= 'n' && s <= 'z') || (s >= 'N' && s <= 'Z'))
						result += Convert.ToChar((s - 13)).ToString();
					else result += s;
				}
				return result;
	  }
	  
	   public static string Rot13(string message)
	   {            
		   return string.Join("", message.Select(x => ConvertChar(x)).ToList());
	   }
	   
	   public static char ConvertChar(int a)
	   {
		   if ( (a >= 'a' && a < 'n') || (a >= 'A' && a < 'N'))
			   return (char)(a + 13);
		   else if ( (a >= 'n' && a <= 'z') || (a >= 'N' && a <= 'Z'))
			   return (char)(a - 13);          
		   else
			   return (char)(a);
	   }
	   
	   ///////////////// 
	  private const string LOWER = "abcdefghijklmnopqrstuvwxyz";
	  private const string UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

	  public static string Rot13(string message)
	  {
		return String.Join("", message
		  .Select(c =>
		  {
			var chars = Char.IsUpper(c) ? UPPER : LOWER;
			var idx = chars.IndexOf(c);
			return idx == -1 ?
			  c :
			  chars[(idx + 13) % chars.Length];
		  }));
	  }
}