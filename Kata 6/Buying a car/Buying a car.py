def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    currentPrice=startPriceOld
    month=0
    percent=1-percentLossByMonth*0.01
    
    while currentPrice < startPriceNew:
        month+=1           
        if month %2==0:
            percent=percent-0.5*0.01 
        startPriceOld*=percent 
        startPriceNew*=percent           
        currentPrice=savingperMonth*month+startPriceOld     
            
    return [month,round(currentPrice-startPriceNew)]