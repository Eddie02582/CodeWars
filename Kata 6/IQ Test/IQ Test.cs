/*

Assert.AreEqual(3, IQ.Test("2 4 7 8 10"));
Assert.AreEqual(1, IQ.Test("1 2 2"));
*/
using System;
using System.Linq;
using System.Collections.Generic;

public class IQ
    {	
				
		public static int Test1(string numbers)
        { 
            var ints = numbers.Split(' ').Select(int.Parse).ToList();
            var unique = ints.GroupBy(x => x % 2).OrderBy(y => y.Count()).First().First();
            return ints.FindIndex(c => c == unique) + 1;
        }
		
		 public static int Test2(string numbers)
		{ 
			var nums = numbers.Split(' ').Select((s, i) => new { Value = int.Parse(s), Index = i });
			var even = nums.Where(x => x.Value % 2 == 0);
			var odd = nums.Where(x => x.Value % 2 == 1);
			return even.Count() == 1 ? even.First().Index + 1: odd.First().Index + 1; 
		}
    }