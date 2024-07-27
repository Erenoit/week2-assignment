points = [
    (1, 2),
    (5, 9),
    (4, 6),
    (7, 8),
    (-73, -89),
    (-49, -31),
    (-41, 11),
    (-31, 19),
    (-7, 7),
    (0, 0),
    (1, 2),
    (99, 99),
    (29, -57),
]

distances = []

def euclideanDistance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def main():
    global points
    global distances

    for i in range(0, len(points) - 1):
        distances.append(euclideanDistance(points[i], points[i + 1]))

    print("Minimum distance:", min(distances))

if __name__ == "__main__":
    main()
