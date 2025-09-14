import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    for _ in range (n):
        word = input().strip()
        res = word[0]+str(len(word)-2)+word[-1] if len(word)>10 else word
        print(res)
if __name__ == "__main__":
    solve()