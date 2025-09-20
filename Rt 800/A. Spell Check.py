#https://codeforces.com/contest/1722/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=input().strip()
        if n!=5:
           print("NO")
           continue
        Timur=["T","i","m","u","r"]
        for i in range(5):
                
                if (s[i] in Timur):
                    Timur.remove(s[i])
                else:
                    break            
        print("YES") if (len(Timur)==0) else print("NO")
       

if __name__ == "__main__":
    solve() 