#https://codeforces.com/contest/1829/problem/A
import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        difference = 0
        if s[0] != "c":
            difference += 1
        if s[1] != "o":
            difference += 1
        if s[2] != "d":
            difference += 1
        if s[3] != "e":
            difference += 1
        if s[4] != "f":
            difference += 1
        if s[5] != "o":
            difference += 1
        if s[6] != "r":
            difference += 1
        if s[7] != "c":
            difference += 1
        if s[8] != "e":
            difference += 1
        if s[9] != "s":
            difference += 1
        print(difference)  
if __name__ == "__main__":
    solve()