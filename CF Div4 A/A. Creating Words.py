#https://codeforces.com/contest/1985/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        a,b=map(str,input().split())
        print(b[0]+a[1:]+" "+a[0]+ b[1:])
        
if __name__ == "__main__":
    solve()