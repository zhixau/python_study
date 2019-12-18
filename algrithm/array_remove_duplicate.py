class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert isinstance(nums, list)

        i = 0
        new_nums = []
        while (i < len(nums)):
            new_nums.append(nums[i])
            if nums.count(nums[i]) > 1:
                i = i + nums.count(nums[i])
            else:
                i = i + 1

        return (len(new_nums), new_nums)


class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert isinstance(nums, list)

        i = 0
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums.remove(nums[i + 1])
            else:
                i = i + 1

        return (len(nums), nums)


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert isinstance(nums, list)

        temp_nums = nums.copy()
        j = 0
        for i in range(0, len(temp_nums)):
            if i < len(temp_nums) - 1 and temp_nums[i] == temp_nums[i + 1]:
                nums.remove(nums[i + 1 - j])
                j = j + 1

        return (len(nums), nums)

class Solution3(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert isinstance(nums, list)

        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    s = Solution3()
    # nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    new_length = s.removeDuplicates(nums)

    print(new_length)
