# https://codeforces.com/problemset/problem/71/A
print(*map(
    lambda w: w[0] + str(len(w[1:-1])) + w[-1] if len(w) > 10 else w,
    (input() for i in range(int(input())))
), sep='\n')
