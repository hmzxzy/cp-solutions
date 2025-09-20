#https://codeforces.com/contest/1692/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        a,b,c,d=map(int,input().split())
        print(0 + (a < b) + (a < c) + (a<d))
if __name__ == "__main__":
    solve()