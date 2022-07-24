# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

altitude = [0]
total = 0
ls = list(map(int,input().split()))

for i in range(n):
    total = total + ls[i]
    altitude.append(total)

print(max(altitude))
