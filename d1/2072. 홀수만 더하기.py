#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    sum = 0
    for i in li:
        if i % 2 != 0:
            sum += i
    print("#" + str(test_case), sum)