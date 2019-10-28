# Hunter Schafer (hschafer)
# This program demonstrates how to profile code in Python


def max_diff1(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    max_diff = 0
    for n1 in nums:
        for n2 in nums:
            diff = abs(n1 - n2)
            if diff > max_diff:
                max_diff = diff
    return max_diff


@profile
def max_diff2(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return abs(max_num - min_num)


@profile
def max_diff3(nums):
    """
    Returns the largest difference between any two numbers in the given list.

    Assumes there is at least one number in the list.
    """
    return max(nums) - min(nums)


@profile
def main():
    nums = list(range(5000))
    print(max_diff1(nums))
    print(max_diff2(nums))
    print(max_diff3(nums))


if __name__ == '__main__':
    main()
