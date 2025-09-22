#https://codeforces.com/contest/2065/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        s = list(input().strip())
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                s.pop(i+1)
            else:
                i += 1  
        print(len(s))
if __name__ == "__main__":
    solve()