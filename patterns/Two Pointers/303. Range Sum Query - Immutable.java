class NumArray {
  public int[] arr2; 
  public NumArray(int[] nums) {
    arr2 = new int[nums.length+1];
    for(int i =0; i<nums.length; i++){
      arr2[i+1]=arr2[i]+nums[i];
    }
  }
  
  public int sumRange(int left, int right) {
    return arr2[right+1]-arr2[left];
  }
}
