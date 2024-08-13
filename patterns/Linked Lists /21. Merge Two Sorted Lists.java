// https://leetcode.com/problems/merge-two-sorted-lists/description/
// O(n) time and O(n) space 
// Tags Linked List Recursion 


class Solution {
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    // check if either null 
      if(list1!=null && list2!=null){
        // add the lower value to the list
        if(list1.val<list2.val){
            // recurse through the list, with list1's value removed
            list1.next=mergeTwoLists(list1.next,list2);
            // return the list1 which contains 1 node 
            return list1;
        }
        else{
            // recurse through the list, with list2's value removed
            list2.next=mergeTwoLists(list1,list2.next);
            // return the list1 which contains 1 node 
            return list2;
        }
      }
      // if unevenly sized then add rest of list2 or list1 whichever is left    
      if(list1==null) 
      return list2;
      return list1;
  }
}