# 📘 Assignment: Algorithm Challenge Lab

## 🎯 Objective

Strengthen your algorithmic problem-solving skills by implementing and comparing multiple search and sort strategies in Python. You will measure performance, explain trade-offs, and choose the best approach for different input sizes.

## 📝 Tasks

### 🛠️ Build Search Algorithms

#### Description
Implement two search functions for a list of student scores: linear search and binary search. Start with small examples to verify correctness, then test both functions with larger lists.

#### Requirements
Completed program should:

- Implement `linear_search(numbers, target)` that returns the index of `target` or `-1`
- Implement `binary_search(sorted_numbers, target)` that returns the index of `target` or `-1`
- Ensure binary search works only on sorted input and document this assumption in comments
- Include at least 3 test cases for found and not-found targets


### 🛠️ Compare Sorting Strategies

#### Description
Implement two sorting algorithms and compare their behavior on the same datasets. Use your code to sort random numbers and nearly sorted numbers to observe differences in operation counts and runtime.

#### Requirements
Completed program should:

- Implement `bubble_sort(numbers)` that returns a new sorted list
- Implement `insertion_sort(numbers)` that returns a new sorted list
- Track simple metrics (comparisons and swaps/shifts) for each algorithm
- Print a clear side-by-side summary of results for at least 2 dataset types


### 🛠️ Analyze and Optimize

#### Description
Create an experiment runner that generates datasets of multiple sizes, runs your search and sort algorithms, and reports runtime trends. Use your results to explain when one algorithm is better than another.

#### Requirements
Completed program should:

- Generate datasets of at least 3 different sizes (for example: 100, 1000, 5000)
- Measure execution time using Python timing tools (such as `time.perf_counter`)
- Summarize results in a readable table printed to the console
- Write a short conclusion in code comments describing which algorithms scale better and why
