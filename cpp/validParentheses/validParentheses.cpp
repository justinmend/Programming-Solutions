/********************************************************************************** 
* 
* Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
* determine if the input string is valid.
* 
* An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* 
* Note that an empty string is also considered valid.
* 
* Example 1:
* Input: "()"
* Output: true
* 
* Example 2:
* Input: "()[]{}"
* Output: true
*
* Example 3:
* Input: "(]"
* Output: false
*
* Example 4:
* Input: "([)]"
* Output: false
*
* Example 5:
* Input: "{[]}"
* Output: true
**********************************************************************************/

#include <iostream>
#include <string>
#include <stack>
#include <map>
using namespace std;

bool isValid(string s)
{
    /* 
    Implement using a stack
    Assumptions: 
    1.Only given valid bracket characters for input. 
    2.Empty string is considered valid parentheses.
    */

    /*
    1.Map the character brackets?
    2.When encountering a closed bracket, pop an item from the stack then
    check if the popped item is equivalent to the mapped value of the closed bracket.
    If brackets don't match return false.
    
    3.After iterating through string s, stack must be empty.
    If stack is empty return true else return false.
    */

    map<char, char> my_dict;
    my_dict['('] = ')';
    my_dict['{'] = '}';
    my_dict['['] = ']';

    stack<char> my_stack;
    for (auto ch : s)
    {
        if (ch == '(' || ch == '{' || ch == '[')
            my_stack.push(ch);
        else if (my_stack.empty() || my_dict[my_stack.top()] != ch)
            return false;
        else
            my_stack.pop();
    }

    return my_stack.empty();

    /* 
    Time Complexity - O(n) where n is the amount of characters we iterate through in string s
    Space Complexity - O(n) where n is the amount of open bracket characters pushed into the stack and worst case
    is string s consist of only open brackets meaning we would have to push all characters in string s to the stack.
    */
}

int main(int argc, char **argv)
{
    string s = "{{}{[]()}}";
    if (argc > 1)
    {
        s = argv[1];
    }
    cout << "str = \"" << (s) << "\"" << endl;
    cout << isValid(s) << endl;
}
