#https://codeforces.com/contest/1829/problem/B
import sys
input=sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        long_maximal=0
        res=0        
        for i in range(n):
            if a[i]==0:
                res+=1
                if res>long_maximal:
                    long_maximal=res
            else:
                res=0
        print(long_maximal)
if __name__=="__main__":
    solve()