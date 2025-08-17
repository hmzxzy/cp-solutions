#https://acm.timus.ru/problem.aspx?space=1&num=1001
import sys
import math

input = sys.stdin.readline

def solve():
    a = list(map(int, input().split()))
    for line in sys.stdin:
        if line.strip():  # skip empty lines
            a.extend(map(int, line.split()))
    for i in range(len(a)-1, -1, -1):
        print(f"{math.sqrt(a[i]):.4f}")
if __name__ == "__main__":
    solve()

