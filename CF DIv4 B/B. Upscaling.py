#https://codeforces.com/contest/1950/problem/B
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n=int(input())
        d="##"
        p=".."
        if n==1:
            print(d)
            print(d)
        else:
            pattern1 = (d + p) * n
            pattern2 = (p + d) * n
            line1 = pattern1[:2*n]
            line2 = pattern2[:2*n]
            for i in range(n):
                if i % 2 == 0:
                    print(line1)
                    print(line1)
                else:
                    print(line2)
                    print(line2)
if __name__ == "__main__":
    solve()