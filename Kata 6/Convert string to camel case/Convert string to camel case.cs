using System;
using System.Text.RegularExpressions;
using System.Linq;
public class Kata
{
  public static string ToCamelCase(string str)
  {
    return Regex.Replace(str, @"[_-](\w)", m => m.Groups[1].Value.ToUpper());
  }
  public static string ToCamelCase(string str)
  {   

    //return string.Join("", str.Split('_','-').Select((x,i) => i>0 ? x.Substring(0, 1).ToUpper() + x.Substring(1) : x));
	return string.Join("", str.Split('_','-').Select((x,i) => i==0 ? x:x.Substring(0, 1).ToUpper() + x.Substring(1)));
  }
       
}