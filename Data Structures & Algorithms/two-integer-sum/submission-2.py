class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      listprev={}

      for i ,n in enumerate(nums):
        diff=target-n
        if diff in listprev:
            return [listprev[diff],i]
        listprev[n]=i