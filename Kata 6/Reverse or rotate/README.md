# Reverse or rotate?

The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If
<ul>
    <li>sz is <= 0 or if str is empty return ""</li>
    <li>sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".</li>
</ul>
## Example:

```
    revrot("123456987654", 6) --> "234561876549"
    revrot("123456987653", 6) --> "234561356789"
    revrot("66443875", 4) --> "44668753"
    revrot("66443875", 8) --> "64438756"
    revrot("664438769", 8) --> "67834466"
    revrot("123456779", 8) --> "23456771"
    revrot("", 8) --> ""
    revrot("123456779", 0) --> "" 
    revrot("563000655734469485", 4) --> "0365065073456944"
```

For the first word "Emma" ASCII values are: 69 109 109 97 </br>
After adding 30 the values will be: 99 139 139 127 </br>
As 139 is prime number so "Emma" is a Prime Word. </br>


## Solution
<sol>

```python 
def prime_word(array):
    result=[0]*len(array)
    for index,x in enumerate(array):
        word,add=x
        for c in word:
            value=ord(c)+add 
            is_prime=True
            for i in range(2,int(value**0.5)+1):
                if value % i ==0:
                    is_prime=False
            if is_prime==True and c != 1:
                result[index]=1
                break                 
    return result
```
