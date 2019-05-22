using System;
using System.Linq;
public static class Kata
{
  public static bool IsPangram(string str)
  {
    return string.Join("", str.ToLower().Select(x => x).Where(a => a > 95 && a < 123).OrderBy(z => z).GroupBy(y => y).Select(s => s.Key).ToList())== "abcdefghijklmnopqrstuvwxyz";
    throw new NotImplementedException();
  }
}