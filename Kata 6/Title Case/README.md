# The nth smallest integer
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.</br>

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.</br>


## Arguments (Haskell)

<ul>
    <li>First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.</li>
    <li>Second argument: the original string to be converted.</li>
</ul>

## Arguments (Other languages)

<ul>
    <li>First argument (required): the original string to be converted.</li>
    <li>Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.</li>
</ul>


## Example

```
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
```

## Solution

sol :利用set,再排序,再取出n-1位置

```python 
def title_case(title, minor_words=''):
    words=[ word.lower() for word in minor_words.split(' ')]
    titles=title.split(' ')
    for i,t in enumerate(titles):
        if i!=0 and t.lower()  in words:
            titles[i]=titles[i].lower()
        else:
            titles[i]=titles[i].title()
    return ' '.join(titles) 
```
