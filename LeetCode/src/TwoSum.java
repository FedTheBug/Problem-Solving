public class TwoSum {
    public static int[] twoSum(int[] nums,int target){
        for(int i=0; i< nums.length; i++){
            for(int j=i+1; j< nums.length; j++){
                if (nums[i]+nums[j] == target){
                    return new int[] {i,j};
                }
            }
        }
        return new int[] {-1,-1};
    }

    public static void main(String[] args) {
        int nums[] = new int[]{2, 7, 11, 15};
        int target = 18;
        int newArr[] = new int[2];
        newArr = twoSum(nums, target);
        for(int i=0; i< newArr.length; i++){
        System.out.println(newArr[i]);
        }
    }
}
