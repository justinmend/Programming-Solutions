/*************************************************************************************** 
 *
 * Given a string, find the first non-repeating character in it and return it's index. 
 * If it doesn't exist, return -1.
 * 
 * Examples:
 * s = "leetcode"
 * return 0.
 * 
 * s = "loveleetcode",
 * return 2.
 * 
 * Note: You may assume the string contain only lowercase letters.
 ***************************************************************************************/

class Solution
{
public:
    int firstUniqChar(string s)
    {
        /*
        Implement using a map
        Assumptions:
        1. Input string contains only lowercase letters
        */

        /*
        1. Map the encountered letters to their frequencies
        2. Iterate through the string s again and check in dictionary
        if the current character has frequency of 1. If so return the character's index.
        We will be able to detect the first unique character
        as we are going through string and referencing the dictionary.
        
        3. Return -1 if we succesfuly iterated through the string and did not find
        a unique character.
        */

        map<char, int> letterFreq;
        for (auto ch : s)
        {
            if (letterFreq.find(ch) != letterFreq.end())
            {
                letterFreq[ch] = letterFreq[ch] + 1;
            }
            else
            {
                letterFreq[ch] = 1;
            }
        }
        for (int i = 0; i < s.length(); i++)
        {
            if (letterFreq[s[i]] == 1)
            {
                return i;
            }
        }

        return -1;

        /* 
        Time Complexity - O(n) where n is the amount of characters we iterate through in string s
        Space Complexity - O(n) where n is the amount of characters we map. Worst case is all the characters in our string s
        are unique and we would have to map them all with their own key.
        */
    }
};