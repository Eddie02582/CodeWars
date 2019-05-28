# Beeramid

Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.</br>

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...</br>

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:</br>

1) your referral bonus, and</br>

2) the price of a beer can</br>

For example:

## Examples:

```
beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16
```


## Solution

sol :離開條件bonus<=0 如果bonus<0,則要減１</br>

``` python
def beeramid(bonus, price):
    i = 0
    while bonus > 0:
        i += 1
        bonus -= price * i**2
        if bonus < 0: i -= 1
    return i
```










