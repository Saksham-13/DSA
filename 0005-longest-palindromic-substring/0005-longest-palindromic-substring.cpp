class
 
Solution {

public:
  string
 
longestPalindrome(string s)
 
{
    int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    
    string longest = "";
    int maxLength = 0;
    
    // Base case: single characters are palindromes
    for (int i = 0; i < n; i++) {
      dp[i][i] = true;
      longest = s[i];
      maxLength = 1;
    }
    
    // Check for length 2 palindromes
    for (int i = 0; i < n - 1; i++) {
      if (s[i] == s[i + 1]) {
        dp[i][i + 1] = true;
        longest = s.substr(i, 2);
        maxLength = 2;
      }
    }
    
    // Check for longer palindromes
    for (int k = 3; k <= n; k++) {
      for (int i = 0; i < n - k + 1; i++) {
        int j = i + k - 1;
        if (s[i] == s[j] && dp[i + 1][j - 1]) {
          dp[i][j] = true;
          if (k > maxLength) {
            longest = s.substr(i, k);
            maxLength = k;
          }
        }
      }
    }
    
    return longest;
  }
};