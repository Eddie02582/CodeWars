# Buying a car

Let us begin with an example: </br>

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.</br>

He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases by 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.</br>

Can you help him? </br>

How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over? </br>

Parameters and return of function: </br>

```
parameter (positive int or float, guaranteed) startPriceOld (Old car price)
parameter (positive int or float, guaranteed) startPriceNew (New car price)
parameter (positive int or float, guaranteed) savingperMonth 
parameter (positive float or int, guaranteed) percentLossByMonth

nbMonths(2000, 8000, 1000, 1.5) should return [6, 766] or (6, 766)
```

where 6 is the number of months at the end of which he can buy the new car and 766 is the nearest integer to 766.158 (rounding 766.158 gives 766).

Note:

Selling, buying and saving are normally done at end of month. Calculations are processed at the end of each considered month but if, by chance from the start, the value of the old car is bigger than the value of the new one or equal there is no saving to be made, no need to wait so he can at the beginning of the month buy the new car:

```
nbMonths(12000, 8000, 1000, 1.5) should return [0, 4000]
nbMonths(8000, 8000, 1000, 1.5) should return [0, 0]
```

依題意,假設有2000元,想買新車8000元,每個月可以存1000元,新舊車每個月折損1.5%,每兩個月折損增加0.5%



```
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    currentPrice=startPriceOld
    month=0
    percent=1-percentLossByMonth*0.01
    
    while(currentPrice < startPriceNew):
        month+=1           
        if month %2==0:
            percent=percent-0.5*0.01 
        startPriceOld*=percent 
        startPriceNew*=percent           
        currentPrice=savingperMonth*month+startPriceOld     
            
    return [month,round(currentPrice-startPriceNew)]
```




