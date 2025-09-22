#https://codeforces.com/contest/2009/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        print(b-a)
        
if __name__ == "__main__":
    solve()