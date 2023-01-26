import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    L, U, X = list(map(int, input().split()))
    answer = 0
    if X > U:
        answer = -1
    elif L <= X <= U:
        answer = 0
    else:
        answer = L - X
    print("#" + str(test_case) + " " + str(answer))