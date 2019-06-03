using System.Collections.Generic;
using System.Linq;
using System;
public class Dioph {
	
    public static string solEquaStr(long n)
    {
      int end = (int)Math.Pow(n, 0.5) + 1;
      long p = 0, q = 0;
      long x = 0, y = 0;
      string msg = "";
      List<string> result = new List<string>();
      for (int i = 1; i < end; i++)
      {
          if (n % i == 0)
          {
              p = i;
              q = n / i;
              if ((p + q) % 2 == 0 && (p - q) % 4 == 0)
              {
                  x = (p + q) / 2;
                  y = (q - p) / 4;
                  msg = string.Format("[{0}, {1}]", x, y);
                  result.Add(msg);
              }
      
          }
      
      }
      msg = string.Join(", ", result);
      return "[" + msg + "]";
    }
}