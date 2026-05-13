class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_sort_list = sorted(list(set(nums)))

        count = 1
        max_count = 1

        for i in range(len(unique_sort_list) - 1):
            # if next number is exactly current number + 1
            if unique_sort_list[i] + 1 == unique_sort_list[i + 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        return max_count