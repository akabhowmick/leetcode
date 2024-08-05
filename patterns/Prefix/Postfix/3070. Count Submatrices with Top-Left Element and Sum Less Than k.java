// # https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/
// # difficulty: medium
// # tags: prefix, range query

// # Solution, O(n*m) time and space, can do with just a column prefix array API
class Solution {

    public int[][] sumMatrix;
    public int subMatrixCount = 0;

    public int countSubmatrices(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        sumMatrix = new int[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                sumMatrix[i][j] = sumMatrix[i - 1][j] + sumMatrix[i][j - 1] - sumMatrix[i - 1][j - 1] + matrix[i - 1][j - 1];
                if (sumMatrix[i][j] <= k) {
                    subMatrixCount++;
                }
            }
        }
        return subMatrixCount;
    }
}
