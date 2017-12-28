dict = {'A': 0, 'B': 0, 'C': 0}
nums = input().split()
nums = [int(x) for x in nums]
nums.sort()
dict['A'] = nums[0]
dict['B'] = nums[1]
dict['C'] = nums[2]
order = input()
print('%d %d %d' % (dict[order[0]],dict[order[1]],dict[order[2]]))
