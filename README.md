# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## My Implementation

For this assignment, I implemented Bubble Sort and Merge Sort in Python. I tested both algorithms with two different datasets and compared their results. I also tested empty, already sorted, and duplicate-value lists.

## Real-World Application

I used streaming content scores as a real-world example. A streaming platform could sort movies or shows by popularity, ratings, or viewing activity before displaying recommendations to users.

## Edge Cases

I tested an empty list to make sure both algorithms returned an empty result without errors. I also tested an already sorted list and a list containing duplicate values. Both algorithms handled these cases correctly.

## Discussion Board Reflection

This assignment helped me understand how Bubble Sort and Merge Sort can produce the same sorted result while using very different approaches. Bubble Sort was easier for me to follow because it compares neighboring values and swaps them when they are out of order. Merge Sort took more thought because it uses recursion to divide the list into smaller pieces before merging them back together.

The most challenging part was understanding how the recursive calls in Merge Sort eventually reached the base case and returned sorted pieces. Breaking the process into the divide and merge steps made it easier to understand.

Bubble Sort can work well for small or nearly sorted datasets, especially when it stops early if no swaps are needed. However, its typical O(n²) performance becomes inefficient as the dataset grows. Merge Sort scales better at O(n log n), but it requires additional memory for the temporary lists created during merging. For larger datasets, Merge Sort would generally be the more efficient choice.