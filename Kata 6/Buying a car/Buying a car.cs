using System;
public class BuyCar {

	public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingPerMonth, double percentLossByMonth) {
		// your code
       double dcurrentPrice = startPriceOld;
       int month = 0;
       double dPriceNew = startPriceNew;
       double dPriceOld = startPriceOld;
       
       double percent = 1 - percentLossByMonth * 0.01;
       while (dcurrentPrice < dPriceNew)
       {
           month += 1;
           percent = month % 2 == 0 ? percent - 0.5 * 0.01 : percent;
           dPriceNew *= percent;
           dPriceOld *= percent;
           dcurrentPrice = savingPerMonth * month + dPriceOld;
       }
       return new int[] { month, (int)Math.Round(dcurrentPrice - dPriceNew) };
	}
}
