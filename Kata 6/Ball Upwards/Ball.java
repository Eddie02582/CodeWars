public class Ball {

    public static int maxBall(int v0) {
        // your code
        double dv0= (double)v0*1000/3600;
        double t=dv0/9.81;
        return (int)Math.round(t * 10);
    }
}