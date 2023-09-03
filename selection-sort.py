def selection_sort(elements):
    """
    Sorts a list of elements using the Selection Sort algorithm.
    
    Parameters:
        elements (list): The list of integers to be sorted.
        
    Returns:
        None: The list is sorted in-place.
    """
    
    # Loop through the entire list
    for i in range(len(elements)):
        # Assume the smallest element is at index i
        smallest_idx = i
        
        # Loop through the remaining elements to find the smallest one
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[smallest_idx]:
                smallest_idx = j
        
        # Swap the smallest element found with the element at index i
        elements[i], elements[smallest_idx] = elements[smallest_idx], elements[i]

# Test the function
elements = [78, 12, 15, 8, 61, 53, 23, 27]
selection_sort(elements)
print("Sorted list:", elements)