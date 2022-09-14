def main():
    target = 0
    nums_copy = nums.copy()
    less_nul = False

    for item in nums:
        # if item > target and item >= 0 and not less_nul:
        #     nums_copy.remove(item)
        if item <= 0:
            less_nul = True
            break
    print(less_nul)
    if not less_nul:
        for item in nums:
            if item > target:
                nums_copy.remove(item)
 
    print(nums_copy)
    for item_1 in nums_copy:
        for item_2 in nums_copy[nums_copy.index(item_1) + 1:]:
            print(item_1)
            print(item_2)
            if item_1 + item_2 == target:
                i = nums.index(item_1)
                del nums[i]
                print([i, nums.index(item_2)+1])
                return

            

main()

