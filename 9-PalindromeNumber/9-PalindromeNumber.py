# Last updated: 08/07/2026, 20:50:52
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        num_array = list(num_str)
        reversed_array = num_array[::-1]
        return num_array == reversed_array

sol = Solution()
input_number = 12321
print(sol.isPalindrome(input_number))  
