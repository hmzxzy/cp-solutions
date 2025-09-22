#https://codeforces.com/contest/1807/problem/A
import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        a,b,c = map(int,input().split())
        print("+") if a+b==c else print("-")
if __name__ == "__main__":
    solve()