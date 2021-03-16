#!/usr/bin/env python3

N = 20

harmonies = [1, 1/8, 1/4, 1/3, 1/2, 2/3, 15/8]
harmonies = [f"{h:.4f}" for h in harmonies]


def check(N):
    print(N)
    total = 0
    for i in range(1, N+1):
        o = N // i
        h = (N / i) % 1
        h = f"{h:.4f}"
        u = h in harmonies
        if u:
            total += 1
        print(i, o, h, "*" if u else "")
    # print(total)
    print(total/N)

print(harmonies)
check(N)

# for i in range(8, 27):
#     check(i)
#     print("//////////")
