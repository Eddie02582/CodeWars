using System.Linq;
using System;
using System.Text.RegularExpressions;
using System.Net;
namespace Solution
  {
  class Kata
    {
      public static bool is_valid_IP(string IpAddres)
      {
        //Code here
         uint numbers=0;        
         return IpAddres.Split('.').Where(x => uint.TryParse(x, out numbers) == true && numbers<256 && numbers.ToString() == x.ToString()).Count() == 4;
      }
	  
	  public static bool is_valid_IP(string IpAddres)
      {
        return Regex.IsMatch(IpAddres, @"^[1-2]?(?<!0)[0-9]{0,2}\.[1-2]?(?<!0)[0-9]{0,2}\.[1-2]?(?<!0)[0-9]{0,2}\.[1-2]?(?<!0)[0-9]{0,2}$");         
      }
	  
	   public static bool is_valid_IP(string IpAddres)
       {
            System.Net.IPAddress ip;
            bool validIp = System.Net.IPAddress.TryParse(IpAddres, out ip);
            return validIp && ip.ToString() == IpAddres;
       }
    }
  }