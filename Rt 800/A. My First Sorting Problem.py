#https://codeforces.com/contest/1971/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        x,y=map(int,input().split())
        print(x,y) if x<y else print(y,x)
        
if __name__ == "__main__":
    solve()