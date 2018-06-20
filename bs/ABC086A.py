#https://beta.atcoder.jp/contests/abs/tasks/abc086_a
a,b = map(int, input().split())

sum_num = (a * b) % 2

if sum_num == 1:
    print("Odd")
else:
    print("Even")
