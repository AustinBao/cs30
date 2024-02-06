import math

def distanceformula(vertex1, vertex2):
    x1, y1 = vertex1[0], vertex1[1]
    x2, y2 = vertex2[0], vertex2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) 
    

vertices = {}
vertexnames = ["A", "B", "C"]
for i in range(3):
    print(f"Vertex {vertexnames[i]}")
    x = int(input(f"Enter x-coordinate for vertex {vertexnames[i]}: "))
    y = int(input(f"Enter y-coordinate for vertex {vertexnames[i]}: "))

    vertices[vertexnames[i]] = (x,y)


distances = []
distances.append(distanceformula(vertices["A"], vertices["B"]))
distances.append(distanceformula(vertices["B"], vertices["C"]))
distances.append(distanceformula(vertices["C"], vertices["A"]))

print(f"AB = {distances[0]}")
print(f"AC = {distances[2]}")
print(f"BC = {distances[1]}")
print(f"Perimeter = {distances[0] + distances[1]  + distances[2]}")

