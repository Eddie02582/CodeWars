using System;
public static class Kata
{
    public static Tuple<char?, int> LongestRepetition(string input)
    {
          if (input == string.Empty)
                return new Tuple<char?, int>(null, 0);

            char[] s = input.ToCharArray();
            int Count=1;
            int temp=0;
            char q = s[0];
            for (int i = 0; i < s.Length; i++)
            {
                Count = 1;
                for (int j = i + 1; j < s.Length; j++)
                {
                    if (s[i] == s[j])
                    {
                        Count = Count + 1;
                    }
                    else
                        break;
                }
                q = Count > temp ? s[i] : q;
                temp = Count > temp ? Count : temp;
                
            }

            return new Tuple<char?, int>(q, temp);
            throw new NotImplementedException("Implement me!");
           
    }
	 public static Tuple<Char?, Int32> LongestRepetition( String input )
	 {
        return input
               .Select( ( x, i ) => new Tuple<Char?, Int32>( x, input.Substring( i ).TakeWhile( y => y == x ).Count() ) )
               .OrderByDescending( x => x.Item2 )
               .FirstOrDefault()
           ?? new Tuple<Char?, Int32>( null, 0 );
	 }
	
}