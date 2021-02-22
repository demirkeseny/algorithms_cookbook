import math


def distance(p1, p2):
    """
    calculating the distance between two points
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute_force(points):
    """
    finding the closest pair among a list of points with (x, y) coordinates
    """
    # assign first two values
    p1 = points[0]
    p2 = points[1]

    # take the first distance as the min
    min_distance = distance(points[0], points[1])

    # if these first two are the only points, return them
    if len(points) == 2:
        return p1, p2, min_distance

    # iterate i until the length-1
    for i in range(len(points) - 1):
        # iterate j from 1 until the end
        for j in range(i + 1, len(points)):

            # if new d is smaller than the min distance, we have a new min distance
            d = distance(points[i], points[j])
            if d < min_distance:
                p1, p2, min_distance = points[i], points[j], d

    return p1, p2, min_distance

def closest_pair(px, py):
    """
    find the closet pair with O(nlog(n)) time
    """
    if len(px) <= 3:
        return brute_force(px)

    Lx = px[:len(px) // 2]
    Rx = px[len(px) // 2:]
    midx = px[len(px) // 2][0]

    Ly = [ly for ly in py if ly[0] <= midx]
    Ry = [ry for ry in py if ry[0] > midx]

    l1, l2, dist1 = closest_pair(Lx, Ly)
    r1, r2, dist2 = closest_pair(Rx, Ry)

    (p1, p2, delta) = (l1, l2, dist1) if dist1 < dist2 else (r1, r2, dist2)

    (t1, t2, dist) = closest_split_pair(px, py, delta, p1, p2)

    if dist < delta:
        return t1, t2, dist
    else:
        return p1, p2, delta

def closest_split_pair(px, py, delta, p1, p2):
    """
    find the closet split pair
    """
    midx = px[len(px) // 2][0]
    Sy = [p for p in py if midx - delta <= p[0] <= midx + delta]
    best = delta
    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 7, len(Sy))):
            if distance(Sy[i], Sy[j]) < best:
                p1, p2, best = Sy[i], Sy[j], distance(Sy[i], Sy[j])

    return p1, p2, best

def find_closest_pair(points):
    """
    call the `closet_pair()` to find the closet pair after sorting the points by x and y coordinates
    :param points: a list of points in (x, y) coordinates
    :return: two tuples and distance
    """
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair(px, py)
