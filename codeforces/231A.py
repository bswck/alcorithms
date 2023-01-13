# https://codeforces.com/problemset/problem/231/A
print(sum(map(
    lambda line: sum(map(int, line.split())) > 1,
    (input() for i in range(int(input())))
)))
