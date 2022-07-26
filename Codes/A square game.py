# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ls = list(map(int,input().split()))

yashasvi = sorted([x*x for x in ls])
print(*yashasvi)
