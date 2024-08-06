# Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Array Math Geometry 
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1, p2):
            if p1[0] == p2[0]:
                return inf
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        initSlope = slope(coordinates[0], coordinates[1])

        return all(
            slope(coordinates[0], coordinates[i]) == initSlope
            for i in range(1, len(coordinates))
        )
        
# Inside the method, a helper function slope is defined to calculate the slope between two points p1 and p2
# If the x-coordinates of the two points are the same (p1[0] == p2[0]), the slope is set to inf (infinity) to handle vertical lines. Otherwise regular 
# It calculates the slope between the first two points.
# It checks if the slope between the first point and each subsequent point matches the initial slope.