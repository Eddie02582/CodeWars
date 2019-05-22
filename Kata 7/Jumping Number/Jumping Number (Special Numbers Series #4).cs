/*
Number passed is always Positive .

Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers.


1- jumpingNumber(9) ==> return "Jumping!!"


2- jumpingNumber(79) ==> return "Not!!"


3- jumpingNumber(23) ==> return "Jumping!!"

4- jumpingNumber(556847) ==> return "Not!!"



*/
using System;
using System.Numerics;
using System;
using System.Linq;
class Kata
{
    public static string JumpingNumber(int n)
    {
        return n < 10 ? "Jumping!!" : Math.Abs(n%10 - (n/10)%10) != 1 ? "Not!!" : JumpingNumber(n/10);
    }
	
	public static string JumpingNumber2(int number)
    {       
        if (number <=10)
          return "Jumping!!";
        int next=0;        
        int temp=0;
        
        while(number>9)
        {
			 temp=number%10;
             next=(number/10)%10;
             
             if (Math.Abs(next-temp)!=1)
             {
                 return "Not!!";           
             }             
             number=number/10 ;   
        }
        return "Jumping!!";
       
    }
	
	public static string JumpingNumber(int number)
    {       
        if (number <=10)
            return "Jumping!!";
        else if (Math.Abs( number%10-(number/10)%10) !=1)
			      return "Not!!";   
		else
			return JumpingNumber(number/10)  ;  
            
		   
    }
	public static string JumpingNumber(int number)
    {
       if (number<10)
                return  "Jumping!!";
            
       int i = 0;
       var q = number.ToString().ToCharArray();           
       return q.Skip(1).All(x => Math.Abs(x - q[i++])==1)==true? "Jumping!!" :"Not!!";
    }
	public static string JumpingNumber(int number)
    {
       var str = number.ToString();
       return str.Skip(1).Select((x,i) => Math.Abs(x-str[i]) == 1).All(x => x) ? "Jumping!!" : "Not!!";
    }
	
}


