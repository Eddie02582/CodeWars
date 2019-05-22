using System.Linq;
using System;
public class DigPow {
	public static long digPow(int n, int p) {	
    var sum = n.ToString().Sum( x =>Math.Pow ( Char.GetNumericValue(x),p++));
    
     return sum % n == 0 ? Convert.ToInt64((sum/n)) : -1L;
	}
}