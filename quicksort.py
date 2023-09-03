# Version 1
def quick_sort_last_element_pivot(sequence):
    """
    Sorts a list of elements using the Quick Sort algorithm.
    This version uses the last element as the pivot.
    
    Parameters:
        sequence (list): The list of integers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    
    length = len(sequence)
    if length <= 1:
        return sequence
    
    pivot = sequence.pop()
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort_last_element_pivot(items_lower) + [pivot] + quick_sort_last_element_pivot(items_greater)

# Test the function
sequence = [4, 2, 1, 5, 7, 6]
sorted_sequence = quick_sort_last_element_pivot(sequence)
print("Sorted using last element as pivot:", sorted_sequence)


# Version 2
def quick_sort_middle_element_pivot(sequence):
    """
    Sorts a list of elements using the Quick Sort algorithm.
    This version uses the middle element as the pivot.
    
    Parameters:
        sequence (list): The list of integers to be sorted.
        
    Returns:
        list: The sorted list.
    """
    
    length = len(sequence)
    if length <= 1:
        return sequence
    
    pivot_index = length // 2
    pivot = sequence.pop(pivot_index)
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort_middle_element_pivot(items_lower) + [pivot] + quick_sort_middle_element_pivot(items_greater)

# Test the function
sequence = [4, 2, 1, 5, 7, 6]
sorted_sequence = quick_sort_middle_element_pivot(sequence)
print("Sorted using middle element as pivot:", sorted_sequence)