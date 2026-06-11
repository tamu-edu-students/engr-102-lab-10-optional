def no_three_in_line(n):
    points = []
    
    # Strategy: Place points in a staggered fashion
    for i in range(n):
        # Use modulo to stagger points on even and odd rows
        x = i
        y = (2 * i) % n
        points.append((x, y))
    
    return points

# Example usage:
n = 8
points = no_three_in_line(n)
print(points)
