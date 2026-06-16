class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #take the first number in position 0
        #subtract that number from target, save the result
        # if the result is in array return its position and first numbers position

        i = 0

        while True:


            x = target - nums[i]

            if x in nums and nums.index(x) != i:
                list = [i, nums.index(x)]
                return sorted(list)

            i += 1

            if i >= len(nums):
                return -1        