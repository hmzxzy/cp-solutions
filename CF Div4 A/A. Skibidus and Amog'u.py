#https://codeforces.com/contest/2065/problem/A
import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(s[slice(0,-2)] + "i")
if __name__ == "__main__":
    solve()
