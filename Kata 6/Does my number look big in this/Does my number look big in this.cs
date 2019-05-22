using System;
using System.Linq;

public class Kata
{
  public static bool Narcissistic(int value)
  {
     return value.ToString().Sum(x => Math.Pow(Char.GetNumericValue(x), value.ToString().Length)) == value;
  }
}