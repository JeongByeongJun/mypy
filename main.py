from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    result_list=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                result_list.append(i)
                result_list.append(j)
                return result_list