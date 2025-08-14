from collections import Counter
def count_frequencies(nums):
    return list(Counter(nums).items())
nums = [1, 2, 2, 3, 3, 3]
frequencies = count_frequencies(nums)
print(frequencies)


from collections import Counter
def frequency_highlights(num):
    num = [1,2,3,1,2,3,2,1]
    freq = Counter(num)
    return freq

print(frequency_highlights([1, 2, 3, 1, 2, 3, 2, 1]))