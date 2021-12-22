# leet code #1
# https://leetcode.com/problems/two-sum/
class Solution(object):
    def two_sum_brute_force(self, arr: [int], target):
        # time complexity is O(n^2)
        for i in range(0, len(arr)):
            j = i + 1
            for j in range(0, len(arr)):
                if arr[i] + arr[j] == target:
                    return i, j
        return []

    # def two_sum_optimized(self, arr: [int], target):


obj = Solution()
print(obj.two_sum_brute_force([1, 2, 3], 3))
