# # Given a input unsorted array of elements, remove block of any contiguous
# elements i.e output should not have any contiguous elements
# example :
# input =  0,1,1,1,6,4,4,0
# valid ouput = 0,6,0
# invalid output = 0,1,6,4

# So there is another way of doing this solution as we could have done a hash table and keeping the index and then m
#following the same approach however, it's a waste of space O(N) but still be O(N)




# tejas@lamden.io

#Runtime O(N)
#Space O(1) does not grow as we just have the res
def remove_con_ele(nums):

    res = []
    if len(nums) == 1:
        return nums

    if not nums:
        return None

    for idx in range(len(nums)):
        if idx == 0: #beg element checks only right
            if nums[idx] != nums[idx + 1]:
                res.append(nums[idx])
                continue
        elif idx  == len(nums) - 1: #end element checks only left
            if nums[idx] != nums[idx - 1]:
                res.append(nums[idx])
                continue
        elif nums[idx] != nums[idx - 1] and nums[idx] != nums[idx + 1]: #else check the middle elements left and right
            res.append(nums[idx])
    return res

    #This solution fails for [1,2,2,2,3,4] as it prints it backward i.e [4,3,1] we could reverse it, however it's extra work.
    # for idx in range(len(nums) - 1, -1, -1):
    #     if idx == len(nums) - 1:
    #         if nums[idx] != nums[idx - 1]:
    #             res.append(nums[idx])
    #             continue
    #
    #     elif idx == 0:
    #         if nums[idx] != nums[idx + 1]:
    #             res.append(nums[idx])
    #             continue
    #
    #     elif nums[idx] != nums[idx - 1] and nums[idx] != nums[idx + 1]:
    #         res.append(nums[idx])
    #
    # return res




import unittest

class Test(unittest.TestCase):

    def test_contigu_random(self):
        actual = remove_con_ele([0,1,1,1,6,4,4,0])
        expected =  [0,6,0]
        self.assertEqual(actual, expected)

    def test_left_edgecase(self):
        actual = remove_con_ele([0,6,6,6,6])
        expected = [0]
        self.assertEqual(actual, expected)

    def test_right_edgecase(self):
        actual = remove_con_ele([1,1,1,1,6])
        expected = [6]
        self.assertEqual(actual,expected)

    def test_left_and_right_case (self):
        actual = remove_con_ele([1,2,2,3,4])
        expected = [1,3,4]
        self.assertEqual(actual, expected)

    def test_one(self):
        actual = remove_con_ele([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_none(self):
        actual = remove_con_ele([])
        expected = None
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)
