class Solution {
    public int solution_1690_4(String time) {
        if(time.equals("??:??")) return 1440;
        int ans=1;
        if(time.charAt(0)=='?' &amp;&amp; time.charAt(1)=='?') ans*=24;
        else if(time.charAt(0)=='?') ans*=(time.charAt(1)-'0'>=4)?2:3;
        else if(time.charAt(1)=='?') ans *=(time.charAt(0)-'0'>=2)?4:10;
        if(time.charAt(3)=='?') ans *=6;
        if(time.charAt(4)=='?') ans *=10;
        return ans;
    }
}


CPP:

int solution_1690_4(string time) {
        if(time=="??:??") return 1440;
        int ans=1;
        if(time[0]=='?' &amp;&amp; time[1]=='?') ans*=24;
        else if(time[0]=='?') ans*=(time[1]-'0'>=4)?2:3;
        else if(time[1]=='?') ans *=(time[0]-'0'>=2)?4:10;
        if(time[3]=='?') ans *=6;
        if(time[4]=='?') ans *=10;
        return ans;
    }


PY :

def solution_1690_4(self, time: str) -> int:
        if(time=="??:??"): return 1440;
        ans=1;
        if(time[0]=='?' and time[1]=='?'): ans=ans*24;
        elif (time[0]=='?'):  
            if(ord(time[1])-ord('0')>=4): ans =  ans*2; 
            else: ans=ans*3;
        elif (time[1]=='?'):  
            if(ord(time[0])-ord('0')>=2): ans = ans*4;
            else:ans= ans*10;
        if(time[3]=='?'): ans = ans * 6;
        if(time[4]=='?'): ans = ans * 10;
        return ans;CPP