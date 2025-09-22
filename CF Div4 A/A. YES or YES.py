#https://codeforces.com/contest/1703/problem/A
import sys
input = sys.stdin.readline
def solve():
    t=int(input())
    for _ in range(t):
        s=input().strip()
        print ("YES") if (s=="YES" or s=="Yes" or s=="yEs" or s=="yeS" or s=="YEs" or s=="YeS" or s=="yES") else print("NO")
if __name__ == "__main__":
    solve() 