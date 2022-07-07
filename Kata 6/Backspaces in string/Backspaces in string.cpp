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