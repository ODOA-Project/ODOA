#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        map<char, char> m { 
            { '(', ')' },
            { '{', '}' },
            { '[', ']' } };
        
        stack<char> st;
        
        for (auto i : s)
        {
            if (i == '(' || i == '{' || i == '[')
                st.push(m[i]);

            if (i == ')' || i == '}' || i == ']')
            {
                if (st.size() == 0) return false;

                if (st.top() == i) 
                    st.pop();
                else 
                    return false;
            }
                
        }

        return st.size() == 0;
    }
};

int main()
{
    Solution s;
    //string str("(){}[]");
    string str("[");
    
    bool b = s.isValid(str);
    return 0;
}