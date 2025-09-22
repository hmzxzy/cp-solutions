#https://codeforces.com/contest/1742/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print("YES") if a+c==b or a+b==c or b+c==a else print("NO")
if __name__ == "__main__":
    solve()