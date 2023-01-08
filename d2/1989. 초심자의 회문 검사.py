import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    input_str = input()
    if input_str == input_str[::-1]:
        print("#" + str(test_case), 1)
    else:
        print("#" + str(test_case), 0)