# 1 задача 
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# 1*
def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

#2
def roman_to_int(s: str) -> int:
    roman_to_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_to_value[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

#3
def is_monotonic(nums):
    def is_increasing(nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

    def is_decreasing(nums):
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                return False
        return True
    
    return is_increasing(nums) or is_decreasing(nums)
