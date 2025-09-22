#https://codeforces.com/contest/2148/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        x,n=map(int,input().split())
        print(0) if n%2==0 else print(x)
if __name__ =="__main__":
    solve()