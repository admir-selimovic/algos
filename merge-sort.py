def merge_two_sorted_lists(a, b):
    """
    Helper function to merge two sorted lists into a single sorted list.
    
    Parameters:
        a (list): First sorted list.
        b (list): Second sorted list.
        
    Returns:
        list: Merged sorted list.
    """
    merged = []
    i = j = 0

    # Merge elements from both lists until one is exhausted
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Append any remaining elements from both lists
    return merged + a[i:] + b[j:]


def merge_sort(arr):
    """
    Merge Sort is a divide-and-conquer algorithm that splits the array into smaller sub-arrays,
    sorts them, and then merges them back together.
    
    Parameters:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    # Base case: Single-element or empty arrays are already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into left and right halves
    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    # Recursively sort both halves
    l = merge_sort(l)
    r = merge_sort(r)

    # Merge the sorted halves
    return merge_two_sorted_lists(l, r)


# Test the merge sort function
arr = [10, 3, 15, 7, 8, 23, 98, 29]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Should print [3, 7, 8, 10, 15, 23, 29, 98]