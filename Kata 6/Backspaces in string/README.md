# Arraydiff

<a href="https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/cpp">原文</a>

Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"<br>

Your task is to process a string with "#" symbols.<br>

```
Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
```
<a href = "https://github.com/Eddie02582/Leetcode/blob/master/020_Valid%20Parentheses.md">Leetcode 20</a>


## Solution

```c++
#include<unordered_map>
#include <stack>
using namespace std;
std::string cleanString(const std::string &s) {
  std::string result = "";
  for (auto &c : s)
  {
    if (c != '#')
    {
      result.push_back(c);
    }
    else if(!result.empty())
    {
      result.pop_back();
    }
  }
  return result;
    
}
```







