n = int(input())
values = []

for i in range(n):
    time, dist = input().split()
    time = int(time)
    dist = int(dist)
    values.append([time, dist])

values = sorted(values, key=lambda x: x[0])

length = len(values)
maxSpeed = 0

for i in range(length-1):
    speed = abs(values[i+1][1] - values[i][1]) / (values[i+1][0] - values[i][0])
    if speed > maxSpeed:
        maxSpeed = speed

print(maxSpeed)
