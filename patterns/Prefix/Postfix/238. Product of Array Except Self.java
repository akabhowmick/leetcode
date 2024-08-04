
import java.util.Arrays;

class Solution {

    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);
        for (int i = 1; i < nums.length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        int rightPointer = nums[nums.length - 1];
        for (int i = nums.length - 2; i > -1; i--) {
            answer[i] *= rightPointer;
            rightPointer *= nums[i];
        }
        return answer;
    }
}
