function longestConsec(strarr, k) {
    if (strarr.length == 0 || k<=0 ||  strarr.length <k)
        return ""
    var result = "";    
    for (var i = 0 ; i < strarr.length ;i++){
        var temp = strarr.slice(i,i + k).join("");
        result =   result.length >= temp.length ? result:temp
        
    }
    
    return result
}
