"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Make a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Each pass moves larger values toward the end.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare neighboring values.
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )
                swapped = True

        # Stop early if the list is already sorted.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # A list with zero or one item is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves.
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # Merge the sorted halves.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare the next value from each half.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any values that remain after one side is empty.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    popularity_scores = [82, 67, 91, 74, 88, 60, 95, 74]

    print("Original scores:", popularity_scores)
    print("Bubble Sort:", bubble_sort(popularity_scores))
    print("Merge Sort:", merge_sort(popularity_scores))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    viewing_counts = [45, 12, 78, 33, 56, 90, 21]

    print("Original viewing counts:", viewing_counts)
    print("Bubble Sort:", bubble_sort(viewing_counts))
    print("Merge Sort:", merge_sort(viewing_counts))

    # Both algorithms should return the same sorted values.
    print(
        "Results match:",
        bubble_sort(viewing_counts) == merge_sort(viewing_counts),
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # An empty list should remain empty with either algorithm.
    empty_list = []
    print("Bubble Sort empty list:", bubble_sort(empty_list))
    print("Merge Sort empty list:", merge_sort(empty_list))

    # An already sorted list should remain in the same order.
    sorted_list = [10, 20, 30, 40, 50]
    print("Bubble Sort sorted list:", bubble_sort(sorted_list))
    print("Merge Sort sorted list:", merge_sort(sorted_list))

    # Duplicate values should remain in the sorted result.
    duplicate_values = [40, 20, 40, 10, 20]
    print("Bubble Sort duplicates:", bubble_sort(duplicate_values))
    print("Merge Sort duplicates:", merge_sort(duplicate_values))


if __name__ == "__main__":
    main()