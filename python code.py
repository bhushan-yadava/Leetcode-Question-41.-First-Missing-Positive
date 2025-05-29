class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        def swap_elements(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        # Get the length of the list
        list_length = len(nums)
      
        # Iterating through the list to place numbers on their correct positions
        for i in range(list_length):
            # Continuously swap the current element until it's in its correct position
            # or it's out of range [1, n]
            while 1 <= nums[i] <= list_length and nums[i] != nums[nums[i] - 1]:
                swap_elements(i, nums[i] - 1)
              
        # After placing each element in its correct position, or as correct as possible, 
        # traverse the list to find the first missing positive integer
        for i in range(list_length):
            # If the current number isn't the right number at index i, return i + 1,
            # because it is the first missing positive integer
            if i + 1 != nums[i]:
                return i + 1
      
        # If all previous positions contain the correct integers, 
        # then the first missing positive integer is n + 1 
        return list_length + 1
