"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert isinstance(nums, list)
        assert isinstance(target, int)

        if len(nums) < 2:
            return None

        for i in range(0, len(nums)):
            y = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == y:
                    return [i, j]


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert isinstance(nums, list)
        assert isinstance(target, int)

        if len(nums) < 2:
            return None

        for i in range(0, len(nums)):
            y = target - nums[i]
            try:
                j = nums[i + 1::].index(y)
                return [i, i + 1 + j]
            except:
                continue

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution3(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert isinstance(nums, list)
        if len(nums) == 0:
            print(nums)
            return 0
        for item in nums:
            left_nums = nums[nums.index(item) + 1::]
            if item in left_nums:
                left_nums.remove(item)
        print(nums)
        return len(nums)


if __name__ == '__main__':
    # c = Solution2()
    # x = c.twoSum([3, 2, 4], 6)
    # print(x)
    # x = c.twoSum([3, 2, 3], 6)
    # print(x)
    c = Solution3()
    x = c.removeDuplicates([])
    print(x)
    x = c.removeDuplicates([1, 2, 1])
    print(x)
    x = c.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(x)
