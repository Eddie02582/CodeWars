function array_diff(a, b) {
    var result = [];
    for (var i = 0; i<a.length ;i++){
        var bappear = false;
        for (var j = 0 ; j < b.length ; j++){
            if (a[i]== b[j]){
              bappear = true;
              break;
            }
        }
        if (!bappear)
          result.push(a[i]);
        
    }
    return result;
    
}



function array_diff_filter(a, b) {

    //lambda
    //return a.filter(x => !b.includes(x))
    
    return a.filter(function(x){b.indexOf(x)==-1;});   
    
}


/*
1. b.includes(x)
2. b.indexOf(x)
3. b = new Set(b) ,b.has(v)


















*/












