using System;
public class Ball 
{
	
    public static int MaxBall(int v0) 
    {
        double dv0= (double)v0*1000/3600;
        double t=dv0/9.81;
        return (int)Math.Round(t * 10);
        // your code
    }
}