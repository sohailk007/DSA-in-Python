"""
BIG O NOTATION EXPLANATION:
Big O notation describes how the runtime or space requirements of an algorithm grow 
as the input size grows. It helps us analyze algorithm efficiency.

Common Time Complexities:
- O(1)     : Constant time      (Best)
- O(log n) : Logarithmic time   (Excellent)
- O(n)     : Linear time        (Good)
- O(n log n): Linearithmic time (Fair)
- O(n²)    : Quadratic time     (Poor)
- O(2ⁿ)    : Exponential time   (Worst)
- O(n!)    : Factorial time     (Terrible)

Space Complexity: Measures memory usage growth
"""

# ======================= O(1) - CONSTANT TIME =======================
# Runtime doesn't change with input size
def get_first_element(arr):
    """O(1) - Always returns first element regardless of array size"""
    if arr:  # O(1) check
        return arr[0]  # O(1) access
    return None

def constant_time_operations():
    """Various O(1) operations"""
    arr = [1, 2, 3, 4, 5]
    
    # All these are O(1)
    first = arr[0]        # Array indexing
    arr.append(6)         # Append to end of list
    arr.pop()             # Remove from end
    length = len(arr)     # Getting length
    math_ops = 5 + 3 * 2  # Arithmetic operations
    
    return first

print("O(1) - Constant Time Examples:")
print(get_first_element([1, 2, 3, 4, 5]))  # Always returns 1, regardless of array size
print("-" * 50)

# ======================= O(log n) - LOGARITHMIC TIME =======================
# Runtime grows logarithmically with input size (very efficient)
def binary_search(arr, target):
    """O(log n) - Binary search halves search space each iteration"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("O(log n) - Logarithmic Time (Binary Search):")
sorted_arr = list(range(1, 101))  # Array of 100 elements
print(f"Found 42 at index: {binary_search(sorted_arr, 42)}")
print("-" * 50)

# ======================= O(n) - LINEAR TIME =======================
# Runtime grows proportionally with input size
def get_squared_number(numbers):
    """O(n) - Time grows linearly with number of elements"""
    squared_numbers = []
    
    for n in numbers:  # This loop runs n times → O(n)
        squared_numbers.append(n * n)  # Each operation is O(1)
        
    return squared_numbers

def linear_search(arr, target):
    """O(n) - Worst case checks all elements"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("O(n) - Linear Time Examples:")
number = [1, 2, 3, 4, 5, 6, 7]
sq_result = get_squared_number(number)
print(f"Squared numbers: {sq_result}")

num = [4, 5, 4, 2, 66, 7, 77, 88, 90]
print(f"Number 66 found at index: {linear_search(num, 66)}")
print("-" * 50)

# ======================= O(n log n) - LINEarithmIC TIME =======================
# Common in efficient sorting algorithms
def merge_sort(arr):
    """O(n log n) - Divide and conquer sorting algorithm"""
    if len(arr) <= 1:
        return arr
    
    # Split array in half - O(log n) splits
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge sorted halves - O(n) merge
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort - O(n)"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("O(n log n) - Linearithmic Time (Merge Sort):")
unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(unsorted_arr)
print(f"Sorted array: {sorted_arr}")
print("-" * 50)

# ======================= O(n²) - QUADRATIC TIME =======================
# Runtime grows with the square of input size (inefficient for large inputs)
def find_duplicates(numbers):
    """O(n²) - Nested loops compare each element with every other element"""
    for i in range(len(numbers)):  # Outer loop: O(n)
        for j in range(i + 1, len(numbers)):  # Inner loop: O(n) → Total: O(n²)
            if numbers[i] == numbers[j]:
                print(f"Duplicate found: {numbers[i]}")
                break

def bubble_sort(arr):
    """O(n²) - Simple but inefficient sorting algorithm"""
    n = len(arr)
    for i in range(n):  # O(n)
        for j in range(0, n - i - 1):  # O(n) → Total: O(n²)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("O(n²) - Quadratic Time Examples:")
numbers = [3, 6, 2, 4, 3, 6, 8, 9]
find_duplicates(numbers)

small_arr = [64, 34, 25, 12]
print(f"Bubble sort result: {bubble_sort(small_arr.copy())}")
print("-" * 50)

# ======================= O(2ⁿ) - EXPONENTIAL TIME =======================
# Runtime doubles with each additional input (very inefficient)
def fibonacci_recursive(n):
    """O(2ⁿ) - Naive recursive Fibonacci (extremely inefficient)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memoized(n, memo={}):
    """O(n) - Memoized Fibonacci (dramatic improvement)"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

print("O(2ⁿ) vs O(n) - Exponential vs Linear:")
print(f"Naive Fibonacci(10): {fibonacci_recursive(10)}")  # O(2ⁿ)
print(f"Memoized Fibonacci(10): {fibonacci_memoized(10)}")  # O(n)
print("-" * 50)

# ======================= O(n!) - FACTORIAL TIME =======================
# Runtime grows factorially with input size (worst case)
def generate_permutations(arr):
    """O(n!) - Generates all permutations of an array"""
    if len(arr) <= 1:
        return [arr]
    
    permutations = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            permutations.append([arr[i]] + p)
    
    return permutations

print("O(n!) - Factorial Time (Permutations):")
small_input = [1, 2, 3]
permutations = generate_permutations(small_input)
print(f"Permutations of [1, 2, 3]: {permutations}")
print("-" * 50)

# ======================= SPACE COMPLEXITY =======================
def constant_space(n):
    """O(1) Space - Uses fixed amount of memory"""
    total = 0
    for i in range(n):
        total += i  # Only one variable used
    return total

def linear_space(n):
    """O(n) Space - Memory usage grows with input size"""
    result = []
    for i in range(n):
        result.append(i)  # Creates list of size n
    return result

print("Space Complexity Examples:")
print(f"O(1) Space result: {constant_space(5)}")
print(f"O(n) Space result: {linear_space(5)}")
print("-" * 50)

# ======================= PERFORMANCE COMPARISON =======================
import time
import matplotlib.pyplot as plt
import numpy as np

def measure_time_complexity():
    """Demonstrate time complexity differences"""
    sizes = [10, 100, 1000, 10000]
    times = {'O(1)': [], 'O(log n)': [], 'O(n)': [], 'O(n²)': []}
    
    for size in sizes:
        arr = list(range(size))
        
        # O(1) - Constant time
        start = time.time()
        _ = arr[0] if arr else None
        times['O(1)'].append(time.time() - start)
        
        # O(log n) - Binary search (on sorted array)
        start = time.time()
        _ = binary_search(arr, size//2)
        times['O(log n)'].append(time.time() - start)
        
        # O(n) - Linear search
        start = time.time()
        _ = linear_search(arr, -1)  # Worst case
        times['O(n)'].append(time.time() - start)
        
        # O(n²) - Bubble sort (only for smaller sizes)
        if size <= 1000:
            start = time.time()
            _ = bubble_sort(arr.copy())
            times['O(n²)'].append(time.time() - start)
        else:
            times['O(n²)'].append(float('nan'))
    
    return sizes, times

print("Time Complexity Performance Comparison:")
sizes, times = measure_time_complexity()
for i, size in enumerate(sizes):
    print(f"Size {size}: O(1)={times['O(1)'][i]:.8f}s, O(log n)={times['O(log n)'][i]:.8f}s, O(n)={times['O(n)'][i]:.8f}s")

print("\n" + "="*80)
print("KEY INSIGHTS:")
print("1. O(1) and O(log n) scale excellently with large inputs")
print("2. O(n) is acceptable for most practical applications")
print("3. O(n²) becomes impractical for large datasets (>10,000 elements)")
print("4. O(2ⁿ) and O(n!) should be avoided for any non-trivial input sizes")
print("5. Always choose the most efficient algorithm that meets your needs")