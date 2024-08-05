// Leetcode Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/solutions/5431675/java-c-python-dp/
// Time O(mn)
// Space O(mn), can improved to O(min(m,n)) with 1d DP.
// Description: Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

class Solution {

    public int numberOfSubmatrices(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int numSubmatrices = 0;
        int[][] xCount = new int[rows + 1][cols + 1];
        int[][] yCount = new int[rows + 1][cols + 1];
        // make two separate arrays for x count and y count
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // same concept as range sum query => add top and left, subtract topLeft elem and add the current elem if it corresponds to the char desired 
                xCount[i + 1][j + 1] = xCount[i][j + 1] + xCount[i + 1][j] - xCount[i][j] + (grid[i][j] == 'X' ? 1 : 0);
                yCount[i + 1][j + 1] = yCount[i][j + 1] + yCount[i + 1][j] - yCount[i][j] + (grid[i][j] == 'Y' ? 1 : 0);
                if (yCount[i + 1][j + 1] == xCount[i + 1][j + 1] && xCount[i + 1][j + 1] > 0) {
                    numSubmatrices++;
                }
            }
        }
        return numSubmatrices;
    }
}
