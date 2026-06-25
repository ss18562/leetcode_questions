class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        answer = [1] * n

        # Store prefix products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Multiply by suffix products
        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer