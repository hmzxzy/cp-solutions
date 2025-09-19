
#https://codeforces.com/contest/1791/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    cflist=["c","o","d","e","f","o","r","c","e","s"]
    for _ in range(t):
        c=input().strip()
        print("YES") if c in cflist else print("NO")
if __name__ == "__main__":
    solve() 