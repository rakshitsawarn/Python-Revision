from collections import Counter

def frequency_highlights(nums):
    # Step 1: Count frequencies
    freq = Counter(nums)
    
    # Step 2: Find highest and lowest frequency
    highest_frequency = max(freq.values())
    lowest_frequency = min(freq.values())
    
    return freq, highest_frequency, lowest_frequency


nums = [1, 2, 3, 1, 2, 3, 2, 1]
freq, highest, lowest = frequency_highlights(nums)

print("Frequencies:", freq)
print("Highest frequency:", highest)
print("Lowest frequency:", lowest)
