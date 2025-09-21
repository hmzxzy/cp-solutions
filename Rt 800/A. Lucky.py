#https://codeforces.com/contest/1676/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
       s=input().strip()
       print("YES") if int(s[0])+int(s[1])+int(s[2])==int(s[3])+int(s[4])+int(s[5]) else print("NO")
if __name__ == "__main__":
    solve()