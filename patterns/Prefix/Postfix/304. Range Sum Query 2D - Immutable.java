// https://leetcode.com/problems/range-sum-query-2d-immutable/description/
// Difficulty: Medium
// tags: prefix

// Solution
// O(n*m) time to construct the prefix square mapping, O(1) to query. O(n*m) space to store the prefix square mapping.
// Create a prefix sum matrix where each cell represents the sum of the square of elements up and left of it, including that element. To get the sum of a region, we take the cell itself, add the left region, add the top region, and subtract the top left region (which was added twice). To compute a prefix sum, we add the cell to the sum of the left and top regions, and subtract the top left region (which was added twice).
class NumMatrix {

    public int[][] sumMatrix;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        sumMatrix = new int[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                sumMatrix[i][j] = sumMatrix[i - 1][j] + sumMatrix[i][j - 1] - sumMatrix[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1++;
        col1++;
        row2++;
        col2++;
        return sumMatrix[row2][col2] - sumMatrix[row1 - 1][col2] - sumMatrix[row2][col1 - 1] + sumMatrix[row1 - 1][col1 - 1];
    }
}
