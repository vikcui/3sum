# author:  YANG CUI
"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""
def num3(nums):
    """
    :param nums: the input nums array
    :return: a list of lists of all possible triples
    :time complexity: O(n^2)
    :space complexity: O(1)
    """
    # list to return
    resultList = []
    # sort the nums array which takes O(nlogn)
    nums.sort()
    numsLen = len(nums)
    print(nums)
    # basic loop structure to fill in the dict object
    for i in range(numsLen-2):
        # if already positive
        if nums[i] > 0:
            break
        # already counted in previous iteration
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        low = i + 1
        high = numsLen - 1
        while low < high:
            tempStr = nums[i] + nums[low] + nums[high]
            if tempStr == 0:
                resultList.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif tempStr > 0:
                high -= 1
            else:
                low += 1
    return resultList






# print(num3([-1, 0, 1, 2, -1, -4]))