#https://codeforces.com/problemset/problem/151/A
import sys
input =sys.stdin.readline
def solve():
     n, k, l, c, d, p, nl, np = map(int, input().split())
     total_drink = (k * l) // nl
     total_lime = c * d
     total_salt = p // np
     print(min(total_drink, total_lime, total_salt) // n)
if __name__ == "__main__":
    solve()
