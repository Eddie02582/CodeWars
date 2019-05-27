# Prime Word

## Your task
X and Y are playing a game. A list will be provided which contains n pairs of strings and integers. They have to add the integeri to the ASCII values of the stringi characters. Then they have to check if any of the new added numbers is prime or not. If for any character of the word the added number is prime then the word will be considered as prime word.</br>

Can you help X and Y to find the prime words?</br>


## Example:

```
    prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
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
