def polygon_area(coords):
    """
    coords: list of (x, y) tuples for polygon vertices in order
    """
    n = len(coords)
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]  # wrap around
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2

# Example: square with points (0,0), (4,0), (4,4), (0,4)
points = [(0, 0), (4, 0), (4, 4), (0, 4)]
print("Polygon Area:", polygon_area(points))  # Output: 16
