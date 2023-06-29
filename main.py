from week1 import two_sum, is_valid, merge_two_lists, ListNode, ListNode_to_list

if __name__ == '__main__':
    assert two_sum(nums = [2,7,11,15], target = 9) == [0,1]
    assert two_sum(nums = [3,3], target = 6) == [0, 1]
    assert two_sum(nums = [3,2,4], target = 6) == [1, 2]
    print("Passed all the tests for two_sum 🎉")

    assert is_valid(s = "()") == True
    assert is_valid(s = "()[]{}") == True
    assert is_valid(s = "(]") == False
    print("Passed all the tests for is_valid 🎉")

    assert ListNode_to_list(merge_two_lists(None, None)) == []
    assert ListNode_to_list(merge_two_lists(ListNode(1, ListNode(2, ListNode(4))),
                                            ListNode(1, ListNode(3, ListNode(4))))) == [1, 1, 2, 3, 4, 4]
    assert ListNode_to_list(merge_two_lists(None, ListNode())) == [0]
    print("Passed all the tests for merge_two_lists 🎉")