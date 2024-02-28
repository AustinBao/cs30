import math

radius = [0.0005, 0.0004, 0.0003, 0.00025, 0.0002]

resistance = []
for r in radius:
    resistance.append(round((1.77 * 10 ** - 8 * 0.15) / (math.pi * (r ** 2)), 9))

print(resistance)

difference = []
for i in range(len(resistance) - 1):
    j = i + 1
    difference.append(round(resistance[j] - resistance[i], 9))
print(difference)
