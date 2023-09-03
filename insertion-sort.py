def insertion_sort(elements):
    """
    Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
    It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    
    Parameters:
        elements (list): The list of elements to be sorted.
        
    Returns:
        None: The function sorts the list in-place.
    """
    # Loop starts from the second element (index 1)
    for i in range(1, len(elements)):
        # The element to be compared and inserted
        anchor = elements[i]
        
        # Initialize the variable 'j' for inner loop
        j = i - 1

        # Inner loop for shifting the elements
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        
        # Position the 'anchor' at its correct position
        elements[j + 1] = anchor

# Test the insertion sort function
elements = [21, 38, 29, 17]
insertion_sort(elements)
print(elements)  # Should print [17, 21, 29, 38]