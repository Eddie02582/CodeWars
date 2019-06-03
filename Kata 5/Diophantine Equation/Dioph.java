import java.util.*;
public class Dioph {
	
 public static String solEquaStr(long n) {
     
        int end=(int)Math.pow(n, 0.5)+1; 
        long p=0,q=0,x=0, y=0;        
        String msg="";
        ArrayList result = new ArrayList();
        for (int i=1 ;i<end ;i++)
        {
            if (n % i == 0)
            {
                p = i;
                q = n / i;
                if ((p + q) % 2 == 0 && (p - q) % 4 == 0)
                {
                    x =  (p + q) / 2;
                    y =  (q - p) / 4 ;
                    msg=String.format("[%s, %s]", x,y); 
                    result.add(msg); 
                }
            }
        }    
        msg=String.join(", ", result);
        return "["+msg+"]";
  }
	
}