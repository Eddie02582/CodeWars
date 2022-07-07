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