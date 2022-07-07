# Arraydiff

<a href="https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/cpp">原文</a>

```
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
```


<a href = "https://github.com/Eddie02582/Leetcode/blob/master/020_Valid%20Parentheses.md">Leetcode 20</a>


## Solution

```c++
#include<unordered_map>
#include <stack>
using namespace std;
bool valid_braces(std::string braces) 
{    
    unordered_map<char, char> pair = {
        {'(', ')'},
        {'[', ']'},
        {'{', '}'},
    };
    stack<char> myStack;
    for (auto &c : braces){
        if(pair.find(c) != pair.end())
        {
            myStack.push(c);
        }
        else if (myStack.empty() || pair[myStack.top()] !=  c)
        {
            return false;
        }  
        else{
            myStack.pop();  
        }               
    }
    return myStack.empty();
  
  // valid or not valid?
}
```

```c++
#include<unordered_map>
#include <stack>
using namespace std;
bool valid_braces(std::string braces) 
{    
    unordered_map<char, char> pair = {
        {')', '('},
        {']', '['},
        {'}', '{'},
    };
    stack<char> myStack;
    for (auto &c : braces){
        if(pair.find(c) == pair.end() || myStack.empty())
        {
            myStack.push(c);
        }
        else if (myStack.top() != pair[c])
        {
            return false;
        }
        else{
            myStack.pop();  
        }               
    }
    return myStack.empty();
  
  // valid or not valid?
}
```







