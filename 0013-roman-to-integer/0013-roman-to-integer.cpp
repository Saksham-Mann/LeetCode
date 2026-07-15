class Solution {
public:
    int value(char q){
        switch(q){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    int romanToInt(string s) {
        int n= s.length();
        if (n==0) return 0;
        int sum=value(s[n-1]);
        for (int i=n-2;i>=0;i--){
            int next= value(s[i+1]);
            int cur=value(s[i]);
            if (cur<next){
                sum-=cur;
            }
            else{
                sum+=cur;
            }
        }
        return sum;
    }
};