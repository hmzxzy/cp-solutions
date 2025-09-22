#https://codeforces.com/contest/1873/problem/A
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        s=input().strip()
        print("YES") if (s[1]=="c" and s[2]=="b") or (s[0]=="b" and s[1]=="a") or (s[0]=="c" and s[2]=="a") or (s=="abc") else print("NO") 
if __name__ == "__main__":
    solve() 