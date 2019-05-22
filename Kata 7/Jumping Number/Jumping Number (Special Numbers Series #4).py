'''
Number passed is always Positive .

Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers.


1- jumpingNumber(9) ==> return "Jumping!!"


2- jumpingNumber(79) ==> return "Not!!"


3- jumpingNumber(23) ==> return "Jumping!!"

4- jumpingNumber(556847) ==> return "Not!!"



'''
def jumping_number(n):
    if n <10:
        return "Jumping!!"
    elif abs (n%10 - (n/10)%10) is not 1:
        return "Not!!"
    else:
        return jumping_number(n/10)
    return  "Jumping!!"
	
	
def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]