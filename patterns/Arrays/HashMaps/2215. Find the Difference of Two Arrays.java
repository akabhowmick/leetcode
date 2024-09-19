
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

// Tags Arrays Hash Maps
class Solution {

    public List<List<Integer>> findDifference(int[] arr1, int[] arr2) {
        // Create a HashMap to store elements from arr2
        HashMap<Integer, Integer> mpp = new HashMap<>();

        // Initialize a list to store unique elements from arr1
        ArrayList<Integer> list = new ArrayList<>();

        // Initialize the final result as a list of lists
        List<List<Integer>> k = new ArrayList<>();

        // Add all elements of arr2 into the HashMap with value 1
        for (int i : arr2) {
            mpp.put(i, 1);
        }

        // For each element in arr1, check if it is in arr2 (using the HashMap)
        // If it's not, add it to the list and mark it in the HashMap
        for (int i : arr1) {
            if (!mpp.containsKey(i)) {
                list.add(i); // Add element from arr1 to the result list
                mpp.put(i, 1); // Mark the element to avoid duplication
            }
        }

        // Add the list of elements unique to arr1 to the final result
        k.add(list);

        // Reinitialize list and HashMap to find unique elements in arr2
        list = new ArrayList<>();
        mpp = new HashMap<>();

        // Add all elements of arr1 into the HashMap
        for (int i : arr1) {
            mpp.put(i, 1);
        }

        // For each element in arr2, check if it is in arr1 (using the HashMap)
        // If it's not, add it to the list and mark it in the HashMap
        for (int i : arr2) {
            if (!mpp.containsKey(i)) {
                list.add(i); // Add element from arr2 to the result list
                mpp.put(i, 1); // Mark the element to avoid duplication
            }
        }

        // Add the list of elements unique to arr2 to the final result
        k.add(list);

        // Return the final result which contains two lists: 
        // one with elements unique to arr1 and one with elements unique to arr2
        return k;
    }
}
