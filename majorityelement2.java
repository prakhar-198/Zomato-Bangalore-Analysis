class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i],map.get(nums[i])+1);
            }else{
                map.put(nums[i],1);
            }
        }ArrayList <Integer> ans=new ArrayList<>();
        for(Map.Entry<Integer,Integer>mapelement:map.entrySet()){
            int val=mapelement.getValue();
            if(val>(nums.length/3)){
                int a=mapelement.getKey();
                ans.add(a);
            }
        }return ans;
    }
}
