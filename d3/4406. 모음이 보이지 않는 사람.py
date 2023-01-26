import sys
sys.stdin = open("input.txt", "r")

T = int(input())
mo = ['a', 'e', 'i', 'o', 'u']
for test_case in range(1, T + 1):
    s = list(input())
    temp = ''
    for i in s:
        if i not in mo:
            temp += i

    print("#" + str(test_case) + " " + temp)