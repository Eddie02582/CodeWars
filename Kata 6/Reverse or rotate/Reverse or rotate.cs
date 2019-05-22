using System;
using System.Linq;

public class Revrot 
{
   public static string RevRot(string strng, int sz)
   {
       int size = 1;
       if (sz > strng.Length || sz <= 0)
           return "";
       else
           size = strng.Length / sz;

       string[] array = new string[size];

       for (int i = 0; i < size; i++)
       {
           array[i] = strng.Substring(i * sz, sz);
           if (array[i].ToString().ToList().Select(x => Convert.ToInt32(x)).Sum() % 2 == 0)
           {
               char[] temp = array[i].ToCharArray();
              
               //temp.Reverse().ToArray();
               //Array.Reverse(temp);
               array[i] = new string(temp.Reverse().ToArray());
           }
           else
           {
               array[i] = array[i].Substring(1) + array[i].Substring(0, 1);
           }

       }
       return string.Join("", array);
   }
   
    public static string RevRot(string s, int sz)
    {
        if (sz==0||s=="") return "";
        var rs=Enumerable.Range(0,s.Length/sz).Select((x,i)=>s.Skip(i*sz).Take(sz).ToArray());
        var rs1=rs.Select(x=>x.Count(y=>(int)y%2==1)).ToArray();
        return string.Join("",rs.Select((x,i)=>string.Join("",rs1[i]%2==1 ? x.Skip(1).Concat(new char[]{x[0]}) : x.Reverse())));
    }	
	
	public static string RevRot(string strng, int sz)
    {
        if (String.IsNullOrEmpty(strng) || sz <= 0 || sz > strng.Length)
            return String.Empty;
        
       var q= Enumerable.Range(0,strng.Length/sz).
            Select(x=> strng.Substring(x*sz,sz))               
            .Select(
				y=> y.Sum(z=> Convert.ToInt32(z)) %2==0 ?                     
                new string (y.ToCharArray().Reverse().ToArray()): y.Substring(1)+y.Substring(0,1)                 
           
           ).ToList();

        return string.Join("",q);


    }
	
	 public static string RevRot(string strng, int sz)
    {
        if (String.IsNullOrEmpty(strng) || sz <= 0 || sz > strng.Length)
            return String.Empty;

        return
            new String(
                Enumerable.Range(0, strng.Length/sz)
                    .Select(i => strng.Substring(i*sz, sz))
                    .Select(
                        chunk =>
                            chunk.Sum(digit => (int) Math.Pow(int.Parse(digit.ToString()), 3))%2 == 0
                                ? chunk.Reverse()
                                : chunk.Skip(1).Concat(chunk.Take(1)))
                    .SelectMany(x => x)
                    .ToArray());
    }
}