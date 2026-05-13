"""
Algorithm Challenge Lab - Starter Code

Implement core search and sort algorithms, compare their performance,
and print a short report.
"""

import random
import time


# =============================================================================
# TASK 1: Search Algorithms
# =============================================================================

def linear_search(numbers, target):
    """
    Return the index of target in numbers, or -1 if not found.
    """
    # TODO: Implement linear search
    pass


def binary_search(sorted_numbers, target):
    """
    Return the index of target in sorted_numbers, or -1 if not found.

    Assumes sorted_numbers is already sorted in ascending order.
    """
    # TODO: Implement binary search
    pass


# =============================================================================
# TASK 2: Sorting Algorithms
# =============================================================================

def bubble_sort(numbers):
    """
    Sort and return a NEW list using bubble sort.

    Returns:
        tuple: (sorted_list, comparisons, swaps)
    """
    # TODO: Implement bubble sort and track comparisons/swaps
    pass


def insertion_sort(numbers):
    """
    Sort and return a NEW list using insertion sort.

    Returns:
        tuple: (sorted_list, comparisons, shifts)
    """
    # TODO: Implement insertion sort and track comparisons/shifts
    pass


# =============================================================================
# TASK 3: Benchmark and Analysis
# =============================================================================

def build_dataset(size, kind="random"):
    """
    Build a dataset for experiments.

    kind options:
      - "random": fully random values
      - "nearly_sorted": mostly sorted with a few values swapped
    """
    # TODO: Generate and return a dataset of the requested kind
    pass


def time_function(func, *args):
    """
    Time a function call and return (result, elapsed_seconds).
    """
    # TODO: Use time.perf_counter() to measure runtime
    pass


def run_experiments(sizes):
    """
    Run search + sort experiments for each size and print a summary table.
    """
    # TODO: Run and report experiments for each dataset size
    pass


if __name__ == "__main__":
    # Suggested sizes for an advanced comparison.
    test_sizes = [100, 1000, 5000]

    # TODO: Add quick correctness checks before full experiments.
    run_experiments(test_sizes)
