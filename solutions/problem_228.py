def get_largest(nums, prefix=""):
    num_dict = dict()
    for num in nums:
        str_num = str(num)
        fdig = str_num[0]
        if fdig not in num_dict:
            num_dict[fdig] = list()
        num_dict[fdig].append(str_num)

    sorted_arrs = sorted(num_dict.values(), key=lambda x: x[0], reverse=True)
    combined = list()
    for arr in sorted_arrs:
        if len(arr) == 1:
            combined.extend(arr)
            continue

        split_dict = dict()
        for num in arr:
            len_num = len(num)
            if len_num not in split_dict:
                split_dict[len_num] = list()
            split_dict[len_num].append(num)

        sorted_val_arrs = sorted(
            split_dict.values(), key=lambda x: len(x[0]))
        for val_arr in sorted_val_arrs:
            combined.extend(sorted(val_arr, reverse=True))

    return int(prefix.join(combined))


# Tests
assert get_largest([10, 7, 76, 415]) == 77641510


"""
Another way
"""

def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numstr = sorted([str(num) for num in nums])
        # go through the list to rearrage the order
        curr = [numstr[0]]
        for i in range(1, len(nums)):
            if curr[-1] +numstr[i] > numstr[i]+curr[-1]:
                numstr[i-len(curr)] = numstr[i]
                numstr[i] = curr[-1]
            elif curr[-1] +numstr[i] == numstr[i]+curr[-1]:
                curr.append(numstr[i])
            else:
                curr = [numstr[i]]
        
        result = ''.join(reversed(numstr)) 
        if int(result)>0:
            return result
        else:
            return '0'