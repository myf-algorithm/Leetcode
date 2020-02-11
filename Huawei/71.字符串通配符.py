import re

try:
    while 1:
        pattern, s = input(), input()
        pattern = pattern.replace('.', '\\.').replace('?', '.').replace('*', '[0-9A-z]*')
        a = re.findall(pattern, s)
        print(str(bool(len(a) == 1 and a[0] == s)).lower())
except:
    pass

"""
// C++解法：动态规划
#include<iostream>
#include<string>   
#include<cstring>
using namespace std;
bool match_string(string str, string strpattern)
{
    int nStr = str.size();
    int nPatt = strpattern.size();
    int** dp = new int*[nStr + 1];
    for (int k = 0; k <= nStr; k++) {
        dp[k] = new int[nPatt + 1];
        memset(dp[k], 0, (nPatt + 1)*sizeof(int));
    }
    int t = 0;
    while(strpattern[t] == '*')
    {
        for (int i = 0; i <= nPatt; ++i)
        {
            dp[t][i] = 1;
        }
        for (int j = 0; j < nStr; ++j){
            dp[j][t] = 1;
        }
        ++t;
    }
    dp[0][0] = 1;
 
    for (int j = 1; j <= nPatt; ++j)
    {
        for (int i = 1; i <= nStr; ++i)
        {
            if ((strpattern[j - 1] == '?' && str[i - 1] != '\0') || strpattern[j - 1] == str[i - 1]){
                dp[i][j] = dp[i - 1][j - 1];
            }
            else if (strpattern[j - 1] == '*'){
                if (dp[i][j - 1] == 1 || dp[i - 1][j] == 1 || dp[i - 1][j - 1] == 1)
                    dp[i][j] = 1;
            }
        }
    }
 
    bool ret = (dp[nStr][nPatt] == 1 ? true : false);
    for (int k = 0; k <= nStr; k++)
        delete[] dp[k];
    delete dp;
    return ret;
}
int main(int argc, char** argv)
{
    string s1, s2;
    while (cin >> s1 >> s2){
        if (match_string(s2, s1))
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }
    return 0;
}
"""