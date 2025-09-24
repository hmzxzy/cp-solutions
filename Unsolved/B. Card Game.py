#https://codeforces.com/contest/1999/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a1,a2,b1,b2=map(int,input().split())
        if a1!=a2 and b1!=b2:
            if max(a1,a2)>max(b1,b2) and  min(a1,a2)>min(b1,b2):
                res=2
        elif a1==a2 and b1==b2:
                if max(a1,a2)>max(b1,b2) and  min(a1,a2)>min(b1,b2):
                     res=4                
        elif a1==a2 and b1!=b2 or a1!=a2 and b1==b2  :
             if max(a1,a2)>max(b1,b2) and  min(a1,a2)>min(b1,b2):
                  res=3
        else:
             res=0
        print(res)
if __name__ == "__main__":
    solve()