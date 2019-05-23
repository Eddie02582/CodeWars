namespace Solution
{
  class Kata
    {
    public static int find_it(int[] seq) 
      {
          int result=0;
          foreach (var n in seq)
          {
              result ^= n;
          }
          return result;
      }
       
    }
}