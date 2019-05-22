using System.Linq;
class Kata
{
	public static bool tidyNumber (int number)
    {
          // Your Code is Here .... Enjoy !!
            char []s  = number.ToString().ToCharArray();

            for (int i = 1; i < s.Length; i++)
            {
                if (Convert.ToInt32(s[i].ToString()) - Convert.ToInt32(s[i - 1].ToString()) < 0)
                {
                    return false;
                }
            }

            return true;
    }
	public static bool tidyNumber(int number)
    {
       return string.Join("", number.ToString().ToCharArray().Select(x => Convert.ToInt32(x.ToString())).OrderBy(y=>y) )== number.ToString();
    }
	
	public static bool tidyNumber(int number)
    {
       int i = 0;
       var q = number.ToString().ToCharArray();           
       return q.Skip(1).All(x => x - q[i++]>=0);
    }  
   
}