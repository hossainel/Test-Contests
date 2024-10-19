#author @chatgpt
from collections import deque
import sys
input = sys.stdin.read

def max_difference_with_memory(test_cases):
    results = []
    
    for case_number, (n, d, numbers) in enumerate(test_cases, start=1):
        max_diff = 0
        deq_max = deque()  # to store indices of potential max values
        deq_min = deque()  # to store indices of potential min values
        
        for i in range(n):
            # Remove elements not within the last d seconds
            if deq_max and deq_max[0] < i - d + 1:
                deq_max.popleft()
            if deq_min and deq_min[0] < i - d + 1:
                deq_min.popleft()
            
            # Maintain the deque for max
            while deq_max and numbers[deq_max[-1]] <= numbers[i]:
                deq_max.pop()
            deq_max.append(i)
            
            # Maintain the deque for min
            while deq_min and numbers[deq_min[-1]] >= numbers[i]:
                deq_min.pop()
            deq_min.append(i)
            
            # Calculate max difference for the valid window
            if i >= d - 1:  # we can only calculate difference after we have d elements
                max_in_window = numbers[deq_max[0]]
                min_in_window = numbers[deq_min[0]]
                max_diff = max(max_diff, max_in_window - min_in_window)
        
        results.append(f"Case {case_number}: {max_diff}")
    
    return results

def main():
    data = input().splitlines()
    index = 0
    T = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(T):
        n, d = map(int, data[index].split())
        index += 1
        numbers = list(map(int, data[index].split()))
        test_cases.append((n, d, numbers))
        index += 1
    
    results = max_difference_with_memory(test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()
