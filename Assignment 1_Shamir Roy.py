# Name - Shamir Roy

# Task 1
nums = [2, 7, 11, 15]
target = 9


def ArrayTask1(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] + nums[j] == target and i != j):
                return i, j

    return None, None


print(f'Output: \n{ArrayTask1(nums, target)}')

# Time Complexity = O(n*n)
# Space Complexity = O(n)

def ArrayTask2(prices):
    max_profit = prices[0]
    max_index = 0
    min_profit = prices[0]
    min_index = 0

    max_dispersion = max_profit - min_profit

    for i in range(len(prices) - 1):
        if (min_profit > prices[i + 1]):
            min_profit = prices[i + 1]
            min_index = i + 1

        if (prices[i] > min_profit and max_dispersion < max_profit - min_profit):
            max_profit = prices[i]
            max_index = i

    if (min_index < max_index):
        return max_profit - min_profit
    else:
        return 0


prices = [7, 1, 5, 3, 6, 4]

print(f'Output: \n{ArrayTask2(prices)}')


# Time complexity for task2 = O(n)
# Space complexity for task2 = O(n)