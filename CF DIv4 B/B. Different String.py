#https://codeforces.com/contest/1971/problem/B
#barely solved 
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if len(set(s)) == 1:
            print("NO")
        else:
            print("YES")
            i = 0
            while s[i] == s[i+1]:
                i += 1
            print(s[:i] + s[i+1] + s[i] + s[i+2:])
if __name__ == "__main__":
    solve()
