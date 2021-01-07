def end_reachable(arr):
    if len(arr) < 2:
        return True

    for i in range(2, len(arr) + 1):
        if arr[len(arr) - i] >= i - 1:
            return end_reachable(arr[:len(arr) - i + 1])


# Tests
assert end_reachable([1, 3, 1, 2, 0, 1])
assert not end_reachable([1, 2, 1, 0, 0])



def canJump(nums):
	n = len(nums)
	maxReached = 0
	for curr in range(n):
		jumpVal = nums[curr]
		maxReached = max(maxReached, jumpVal+curr)  # update best record
		if maxReached == curr:                      # reached max distance pottential
			break
	return maxReached >= n-1


assert canJump([1, 3, 1, 2, 0, 1])
assert not canJump([1, 2, 1, 0, 0])
