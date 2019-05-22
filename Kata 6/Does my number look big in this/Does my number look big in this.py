def narcissistic( value ):  
   return sum( int(s)**len(str(value)) for s in str(value))==value