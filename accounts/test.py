#code
n = int(input())

for i in range(n):
    inp = list(input().split())
    for i in range(len(inp)):
        inp[i] = int(inp[i])
    val = list(input().split())
    for i in range(len(val)):
        val[i] = int(val[i])
    op = val[inp[1]:] + val[:inp[1]]
    print(op)